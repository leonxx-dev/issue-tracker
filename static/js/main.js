// Adding label to ticket status depend on status
$(document).ready(function(){
    var getLabel = document.getElementsByClassName("status-color");
    for (var i = 0; i < getLabel.length; i++) {
        var status = $(getLabel[i]).first().text();
        var label = getLabel[i];
        if (status == "Pending"){
            label.classList.add("label", "label-info");
        }else if (status == "In Progress"){
            label.classList.add("label", "label-warning");
        }else{
            label.classList.add("label", "label-primary");
        }
    }
});
// Adding label to ticket type depend on type
$(document).ready(function(){
    var getLabel = document.getElementsByClassName("type-color");
    for (var i = 0; i < getLabel.length; i++) {
        var type = $(getLabel[i]).first().text();
        var label = getLabel[i];
        if (type == "Issue"){
            label.classList.add("label", "label-success");
        }else{
            label.classList.add("label", "label-danger");
        }
    }
});
// Removing default options from dropdown menus of ticket_type
$(document).ready(function(){
    $("select[id=id_ticket_type] > option:first-child")
    .remove();
});
//Adding classes to bootstrap forms
$(document).ready(function(){
    var type = document.getElementById("div_id_ticket_type");
    var type_name = document.getElementById("div_id_ticket_type__name");
    var date = document.getElementById("div_id_published");
    var title = document.getElementById("div_id_title");
    var content = document.getElementById("div_id_content");
    var upvotes = document.getElementById("div_id_upvotes");
    var title_contains = document.getElementById("div_id_title_contains");
    $(type_name).addClass("col-xs-6 col-md-2 col-md-offset-2");
    $(type).addClass("col-xs-6 col-md-2 col-md-offset-2");
    $(date).addClass("col-xs-6 col-md-2");
    $(upvotes).addClass("col-xs-6 col-md-2");
    $(title_contains).addClass("col-xs-12 col-md-8 col-md-offset-2");
    $(title).addClass("col-xs-12 col-md-8 col-md-offset-2");
    $(content).addClass("col-xs-12 col-md-8 col-md-offset-2");
});