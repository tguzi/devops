import{c as d,a as f,r as p,o as m,b as _,d as h,e as y}from"./vendor.714eeb62.js";const v=function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))r(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const o of t.addedNodes)o.tagName==="LINK"&&o.rel==="modulepreload"&&r(o)}).observe(document,{childList:!0,subtree:!0});function n(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerpolicy&&(t.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?t.credentials="include":e.crossorigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function r(e){if(e.ep)return;e.ep=!0;const t=n(e);fetch(e.href,t)}};v();const g="modulepreload",i={},L="./",E=function(s,n){return!n||n.length===0?s():Promise.all(n.map(r=>{if(r=`${L}${r}`,r in i)return;i[r]=!0;const e=r.endsWith(".css"),t=e?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${r}"]${t}`))return;const o=document.createElement("link");if(o.rel=e?"stylesheet":g,e||(o.as="script",o.crossOrigin=""),o.href=r,document.head.appendChild(o),e)return new Promise((a,u)=>{o.addEventListener("load",a),o.addEventListener("error",u)})})).then(()=>s())},O=[{path:"/",component:()=>E(()=>import("./index.dddfa5ac.js"),["static/index.dddfa5ac.js","static/index.3bce8336.css","static/vendor.714eeb62.js"])}],b=d({history:f(),routes:O});var k=(c,s)=>{const n=c.__vccOpts||c;for(const[r,e]of s)n[r]=e;return n};const P={};function w(c,s){const n=p("router-view");return m(),_("div",null,[h(n)])}var x=k(P,[["render",w]]);const l=y(x);l.use(b);l.mount("#app");export{k as _};