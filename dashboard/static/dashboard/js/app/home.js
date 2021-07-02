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
        cookie: "/static/dashboard/js/vendor/js.cookie",
        chart: "/static/dashboard/js/vendor/chart-3.4.0.min",
        moment: "/static/dashboard/js/vendor/moment-with-locales",
    }
});

requirejs(["material", "cookie", "chart", "jquery", "base", "moment"], function(mdc, Cookies) {
	require(["chart"], function(Chart){
		console.log("Chart: ");
		console.log(Chart);
	});
});