var curSize = null; // localStorage.getItem("saveSize");
var slider = document.querySelector('.font-slider input[type="range"]')
var body = document.body
var defaultSize = body.style.getPropertyValue('font-size');

if (curSize) {
  var saveSize = curSize;
  document.documentElement.style.setProperty("--font-size", saveSize + "px");
  //body.style.fontSize = saveSize + 'px';
}

slider.addEventListener("input", function(e) {
  var newSize = this.value,
    minSize = 10,
    maxSize = 72;

  if (newSize <= maxSize && newSize >= minSize) {
    document.documentElement.style.setProperty("--font-size", newSize + "px");
    //    body.style.fontSize = newSize + 'px';
    //    localStorage.setItem("saveSize", newSize);
  }
});

const pageMain = document.querySelector(".dynamic");

let __wghtVal = 400;

const wghtInput = document.getElementById("wght");
const wghtSpan = document.getElementById("wghtVal");

const Trigger = new Event("changeVal");

function wghtVal(val = undefined) {
  if (val) {
    __wghtVal = val;
  }
  return `"wght" ${__wghtVal}`;
}

const content = document.querySelector(".dynamic");

window.addEventListener("DOMContentLoaded", (event) => {
  content.dispatchEvent(new Event("changeVal"));
});

content.addEventListener("changeVal", () => {
  content.setAttribute(
    "style",
    `font-variation-settings: ${wghtVal()};`
  );
});

wghtInput.addEventListener(".font-slider", (e) => {
  wghtVal(e.target.value);
  wghtSpan.innerText = __wghtVal;
  content.dispatchEvent(Trigger);
});

function dice() {
  wghtVal(Math.floor(Math.random() * 900) + 100);

  wghtInput.value = __wghtVal;
  wghtInput.dispatchEvent(new Event("input"));
}

document.getElementById("randbutton").addEventListener("click", dice);

function copyElementText(id) {
    var text = document.getElementById(id).innerText;
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = text;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
}
function ShowSecond() {
    var div2 = document.getElementById("div2");
    div2.className = "show";
    setTimeout(function () {
        div2.className = 'hide';
    }, 2000);
}