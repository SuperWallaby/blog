HTMLElement.prototype.hasClass = function (cls) {
    var i;
    var classes = this.className.split(" ");
    for (i = 0; i < classes.length; i++) {
        if (classes[i] == cls) {
            return true;
        }
    }
    return false;
};

function changeLang(index) {
    document.getElementById('LANG_SELECTER').selectedIndex = index;
    document.langForm.submit();
}

function toggleSideNav() {
    var target = document.getElementById('SITE_MENU');
    var root = document.getElementById('root');
    var isOpen = root.hasClass('out')

    target.classList.toggle('hidden');
    root.classList.add('startedNav');
    if (isOpen)
        root.classList.remove('out');
    else
        root.classList.add('out');

    
}

function prevent(e) {
    e.preventDefault();
    e.stopPropagation();
}