requirejs.config({
    shim: {
        jquery: {
            exports: "$"
        },
        cookie: {
            exports: "Cookies"
        },
        bootstrap: {
            deps: ["jquery"]
        },
    },
    baseUrl: "/static/dashboard/js/app",
    paths: {
        app: '/static/dashboard/js/app',
        material: "/static/dashboard/vendor/material-components-web-11.0.0",
        jquery: "/static/dashboard/vendor/jquery-3.4.0.min",
        cookie: "/static/dashboard/vendor/js.cookie"
    }
});

requirejs(["material", "cookie", "jquery"], function(mdc, Cookies) {
    var csrftoken = Cookies.get('csrftoken'); // $("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    const drawer = mdc.drawer.MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));

    const topAppBar = mdc.topAppBar.MDCTopAppBar.attachTo(document.getElementById('app-bar'));

    topAppBar.setScrollTarget(document.getElementById('main-content'));

    topAppBar.listen('MDCTopAppBar:nav', () => {
        drawer.open = !drawer.open;
    });
    
    window.setTimeout(function() {
	    drawer.open = true;
	    console.log("open drawrer");
	}, 50);

    const itemsList = mdc.list.MDCList.attachTo(document.getElementById('home_drawer'));

    itemsList.listen('MDCList:action', function(e) {
    	const path = $(itemsList.listElements[e['detail']['index']]).attr("data-href");

    	window.location = path;
    });
});