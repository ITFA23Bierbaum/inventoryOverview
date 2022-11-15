function disableCheckbox() {
    $('.contentRow > td:last-child > div > input:checked:not(:disabled)').each(function(index, checkbox) {
        checkbox.disabled = true;
    });
}