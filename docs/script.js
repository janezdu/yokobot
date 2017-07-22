$(document).ready(function() {
   $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
    $('.nav-tabs a').on('shown.bs.tab', function(event){
        var x = $(event.target).text();         // active tab
        var y = $(event.relatedTarget).text();  // previous tab
        $(".act span").text(x);
        $(".prev span").text(y);
    });

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

  $('#sortCustom').click(function(){
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
      "simpleweight": $('input[name="simpleweight"]:checked').val() - 0,
      "livelyweight": $('input[name="livelyweight"]:checked').val() - 0,
      "cuteweight": $('input[name="cuteweight"]:checked').val() - 0,
      "pureweight": $('input[name="pureweight"]:checked').val() - 0,
      "coolweight": $('input[name="coolweight"]:checked').val() - 0,
      "tags": selected.slice(0, 2)
    }
    console.log(target)
    var root = 'https://jsonplaceholder.typicode.com';
    $.post(root + '/posts', {}, tablify)
      // var root = 'janezdu.pythonanywhere.com/asdf';
      // $.post(root + '/partial/custom', {wardrobe:wardrobe,target:target}, tablify);
  });

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

  $('#sortPreset').click(function(){
      // var params = {"stage": $('#level').text() };
      // console.log($('$level option:selected').text());
    var params = {
      "stage": "1-1"
    }
    console.log($.param(params));
  });
});

