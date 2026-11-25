import { chromium, webkit, firefox } from "playwright";
import { mkdir } from "node:fs/promises";
const base=process.env.BEEGO_QA_URL??"http://127.0.0.1:4321";
const routes=["/","/como-funciona/","/bateria-beego/","/estaciones/","/negocios/","/ayuda/"];
const variants=[
  ["compacto-320",320,720],["android-360",360,780],["mobile-390",390,844],
  ["mobile-430",430,932],["tablet-768",768,1024],["tablet-1024",1024,768],
  ["laptop-1366",1366,768],["desktop-1440",1440,900],
  ["desktop-1920",1920,1080],["wide-2560",2560,1440],["tv-3840",3840,2160]
];
const checks=[
  {name:"Chromium",engine:chromium,v:variants},
  {name:"WebKit-Safari",engine:webkit,v:[variants[2],variants[4],variants[7]]},
  {name:"Firefox",engine:firefox,v:[variants[2],variants[7]]}
];
const errors=[];let tested=0;
await mkdir("qa/screenshots",{recursive:true});
for(const group of checks){
  const browser=await group.engine.launch({headless:true});
  try{
    for(const [label,width,height] of group.v){
      const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
      for(const path of routes){
        try{
          const response=await page.goto(new URL(path,base).href,{waitUntil:"domcontentloaded",timeout:30000});
          if(!response?.ok())throw Error("HTTP "+response?.status());
          await page.locator("main").waitFor({state:"visible"});
          await page.evaluate(()=>document.fonts?.ready);
          const info=await page.evaluate(()=>{
            const doc=document.documentElement;
            return {viewport:doc.clientWidth,scroll:doc.scrollWidth,
              broken:[...document.images].filter(im=>im.complete&&im.naturalWidth===0).map(im=>im.getAttribute("src")),
              hasTitle:!!document.querySelector("h1")};
          });
          if(info.scroll>info.viewport+3)errors.push(group.name+" "+label+" "+path+" overflow "+info.scroll+"/"+info.viewport);
          if(info.broken.length)errors.push(group.name+" "+label+" "+path+" failed images "+info.broken.join(","));
          if(!info.hasTitle)errors.push(group.name+" "+label+" "+path+" missing h1");
          tested++;
          if(group.name==="Chromium"&&(label==="mobile-390"||label==="desktop-1440")&&
             ["/","/negocios/","/bateria-beego/"].includes(path)){
            const slug=path==="/"?"inicio":path.slice(1,-1);
            await page.screenshot({path:"qa/screenshots/"+label+"-"+slug+".png",fullPage:true,animations:"disabled"});
          }
        }catch(e){errors.push(group.name+" "+label+" "+path+" "+String(e));}
      }
      await page.close();
    }
  }finally{await browser.close();}
}
console.log("BeeGo: ",tested,"páginas/dispositivos evaluados");
if(errors.length){errors.forEach(e=>console.error("FAIL",e));process.exit(1);}
console.log("PASS: sin errores de imágenes o desbordamiento horizontal.");
