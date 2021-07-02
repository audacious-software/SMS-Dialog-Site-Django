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
        material: "/static/dashboard/js/vendor/material-components-web-11.0.0",
        jquery: "/static/dashboard/js/vendor/jquery-3.4.0.min",
        cookie: "/static/dashboard/js/vendor/js.cookie"
    }
});

requirejs(["material", "cookie", "jquery"], function(mdc, Cookies) {
	const username =  mdc.textField.MDCTextField.attachTo(document.getElementById('field_username'));
	const password =  mdc.textField.MDCTextField.attachTo(document.getElementById('field_password'));
    
    var csrftoken = Cookies.get('csrftoken');

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
});