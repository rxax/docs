$(document).ready(() => {
    // get previously selected page
    let selected_page = localStorage.getItem('selected_pages');
    let selection = JSON.parse(selected_page) || [];
    //console.log(selected_page)

    // Open external urls in new window
    $(document.links).filter(function () {
        return this.hostname != window.location.hostname;
    }).attr('target', '_blank');

    // Collapse all trees
    $('ul.tree').toggle();

    // Toggle previously selected page
    $('ul.tree').each(function (){

        let label = $(this).parent().children('label')[0].innerText;
        if(selection.includes(label)) {
            $(this).toggle();
        }
    });

    // Toggle sidebar tree
    $('label.tree-toggler').click(function () {
        $(this).parent().children('ul.tree').toggle(300);

        // Save currently opened page
        let page_name = $(this)[0].innerText;
        //console.log(page_name)
        if(!selection.includes(page_name)) {
            selection.push(page_name);
        } else {
            // remove from selection
             selection = selection.filter(function(value, index, arr) {
                 return value !== page_name;
             });
        }

        // save updated selection
        localStorage.setItem('selected_pages', JSON.stringify(selection));

    });

    // Get current page and set the page anchor to active
    let page = document.location.href.match(/[^\/]+$/)[0]
    $('.page').each(function () {
        if ($(this).attr('href').indexOf(page) !== -1) {
            $(this).addClass('active');
        }
    })
})

