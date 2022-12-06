$( document ).ready(function() {
    [].slice.call(document.getElementsByClassName('close-icon')).forEach(function(e) {
        e.addEventListener("click", function(e) {
            e.srcElement.parentElement.style.display = 'none';
        });
    });

    document.getElementById('icon_show_best_path').addEventListener("click", function(e) {
        document.getElementById('pnl_tsp_best_path').style.display = 'block';
    });
});

function disableCheckbox() {
    $('.contentRow > td:last-child > div > input:checked:not(:disabled)').each(function(index, checkbox) {
        checkbox.disabled = true;
    });
}