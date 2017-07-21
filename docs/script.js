function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}


$("#act").change(function() {
  var el = $(this);
  switch (el.val()) {
    case "Act 1":
      var newOptions = {
        "1-1": "a1l1",
        "1-2": "a1l2",
        "1-3": "a1l3"
      };
      break;
    case "Stylist Arena":
      var newOptions = {
        "Golden Odeum": "goldenodeum",
        "Summer Party": "summerparty",
        "Summer Story": "summerstory"
      };
      break;
    default:
      var newOptions = {}
      break;
  }
  var $el = $("#level");
  $el.empty(); // remove old options
  $.each(newOptions, function(key, value) {
    $el.append($("<option></option>")
      .attr("value", value).text(key));
  });
});

function sortCustomStage() {

  var selected = [];
  $('#tag :checked').each(function() {
    selected.push($(this).attr('value'));
  });
  var wardrobe = {};
  var target = {
      "simple": $('input[name="simplicity"]:checked').val() === "0",
      "lively": $('input[name="liveliness"]:checked').val() === "0",
      "cute": $('input[name="cuteness"]:checked').val() === "0",
      "pure": $('input[name="pureness"]:checked').val() === "0",
      "cool": $('input[name="coolness"]:checked').val() === "0",
      "simpleweight": $('#simpleweight').val() - 0,
      "livelyweight": $('#livelyweight').val() - 0,
      "cuteweight": $('#cuteweight').val() - 0,
      "pureweight": $('#pureweight').val() - 0,
      "coolweight": $('#coolweight').val() - 0,
      "tags": selected.slice(0, 2)
    }
  var root = 'https://jsonplaceholder.typicode.com';
  $.post(root + '/posts', {}, tablify)
   // var root = 'janezdu.pythonanywhere.com/asdf';
  // $.post(root + '/partial/custom', {wardrobe:wardrobe,target:target}, tablify);

}



function tablify(sortedWardrobe) {

  var result = {
    "hair": [1, 2],
    "hosiery": [3, 2, 1]
  }

  var hosieryfilter = [1, 2];
  var ankletfilter = [3];

  function lookup(selector, catlist) {
    catlist.forEach(function(item) {
      $(selector).append(
        "<li>" + item + "</li>")
    });
  }

  lookup('#outHair > ul', result.hair)
  lookup('#outAnklet > ul', result.hosiery.filter(function(n) {
    return hosieryfilter.indexOf(n) !== -1;
  }))

}

function sortPresetStage() {
  // var params = {"stage": $('#level').text() };
  // console.log($('$level option:selected').text());
  var params = {"stage": "1-1"}
  console.log($.param(params));
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();