let counter = 9;
let menu = document.getElementById("navBar");
let screenWidth = screen.width;



//Функция автодополнения
let fun = function(reg) {
  let n = 21;
  $.getJSON("/api/article/get?offset=" + n + "&limit=20&region="+reg, function(data) {
    n += 20;
    for (let i = 0; i < data.length; i++) {
      var items = document.getElementsByClassName("items")[0];
      var div = document.createElement("div");
      div.className = "items__item";
      div.innerHTML = `
              <input class="hide" id="hd-${data[i]["id"]}" type="checkbox">
              <label class="items__item__photo" style="background-image:linear-gradient(#b1b1b13b, #ffffff), url(${data[i]["images"]});" for="hd-${data[i]["id"]}">
                <span class="date">${data[i]["date"]}
                </span><strong><h3>${data[i]["title"]}</h3></strong>
                <p>${data[i]["description"]}</p>
              </label>

              <div>
                  ${data[i]["text"]}
                  <br>
                  <input class="none__two" id="hd-${data[i]["id"]}" type="checkbox">
                  <label class="none__two-two" for="hd-${data[i]["id"]}"><strong>Закрыть</strong></label>
              </div>
              `;
      items.appendChild(div);
    }

    //do nothing
  });
  return false;
};

/**
 Скрипт мобильной шапки
 */
function menuShow() {
  menu.classList.toggle("menuShow");
}

/**
 Скрипт который скрывает мобильную шапку
 */
var header = $("nav"),
  scrollPrev = 0;

let scrol = $(window).scroll(function() {
  let userPosition = Math.round(
    (window.innerHeight + pageYOffset) / document.documentElement.clientHeight
  );

  if (userPosition >= counter) {
    fun(0);
    counter += 9;
  }

  if (screen.width <= 768) {
    var scrolled = $(window).scrollTop();
    if (scrolled > 100 && scrolled > scrollPrev) {
      header.addClass("out");
    } else {
      header.removeClass("out");
    }
    scrollPrev = scrolled;
  }
});

let scrol2 = $(window).scroll(function() {
  let userPosition = Math.round(
    (window.innerHeight + pageYOffset) / document.documentElement.clientHeight
  );

  if (userPosition >= counter) {
    fun(72);
    counter += 9;
  }

  if (screen.width <= 768) {
    var scrolled = $(window).scrollTop();
    if (scrolled > 100 && scrolled > scrollPrev) {
      header.addClass("out");
    } else {
      header.removeClass("out");
    }
    scrollPrev = scrolled;
  }
});

function clock() {
  var d = new Date();
  var month_num = d.getMonth();
  var day = d.getDate();
  var hours = d.getHours();
  var minutes = d.getMinutes();

  month = new Array(
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря"
  );

  if (day <= 9) day = "0" + day;
  if (hours <= 9) hours = "0" + hours;
  if (minutes <= 9) minutes = "0" + minutes;

  date_time =
    "Сегодня - " +
    day +
    " " +
    month[month_num] +
    " " +
    d.getFullYear() +
    " г.&nbsp;&nbsp;&nbsp; <br> Текущее время - " +
    hours +
    ":" +
    minutes;
  if (document.layers) {
    document.layers.doc_time.document.write(date_time);
    document.layers.doc_time.document.close();
  } else document.getElementById("doc_time").innerHTML = date_time;
  setTimeout("clock()", 1000);
}
