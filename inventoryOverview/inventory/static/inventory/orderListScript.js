$( document ).ready(function() {
    $('#frm_content').submit(function(e){
        $.post('/orderList', $(this).serialize(), function(data){
           $('#tbl_orders_body').replaceWith($(jQuery.parseHTML(data)).find('#tbl_orders_body'));
        });
        e.preventDefault();
    });
});

function filter(event) {
    if (event.keyCode >= 48 && event.keyCode <= 57
            || event.keyCode >= 65 && event.keyCode <= 90
            || event.keyCode == 8) {
        document.getElementById('hidden_filter').value = 'active';
        $('#frm_content').submit();
        document.getElementById('hidden_filter').value = '';
    }
}

function orderClick(orderNo) {
    document.getElementById('input_redirectValue').value = orderNo;
    frm_redirect.submit();
}