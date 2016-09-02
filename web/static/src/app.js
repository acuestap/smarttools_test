(function (ng) {
    /*
    var smarttoolsAPP = ng.module('smarttoolsAPP', [
        'ngRoute',
        'competitionModule',
        'webModule',
        'clientsModule'
    ]);
    */
    var smarttoolsAPP = ng.module('smarttoolsAPP', [
        'ngRoute',
        'competitionModule',
        'webModule',
        'clientsModule',
        'ngCookies'
    ]).run(
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        // Add the following two lines
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    });

    // smarttoolsAPP.config(['$interpolateProvider', '$routeProvider', '$httpProvider', function ($interpolateProvider, $routeProvider, $httpProvider) {
    // smarttoolsAPP.config(['$interpolateProvider', '$routeProvider', function ($interpolateProvider, $routeProvider)

    smarttoolsAPP.config(['$interpolateProvider', '$routeProvider', '$httpProvider', function ($interpolateProvider, $routeProvider, $httpProvider) {
        //Configuracion necesaria para el manejo del CRUD de django-angular
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        // configuramos los símbolos para poder llamar los {} por []
        // ya que eventualmente ponen problemas y no cargan la info del scope
        // tomado de: http://pythoniza.me/configuracion-de-angular-en-proyecto-django/

         $interpolateProvider.startSymbol('[[');
         $interpolateProvider.endSymbol(']]');


        $routeProvider
            .when('/', {
                templateUrl:'/static/src/modules/web/web.tpl.html',
                controller: 'webCtrl'
            })
            .when('/competitions', {
                templateUrl:'static/src/modules/competitions/competition.tpl.html',
                controller: 'competitionCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise({redirectTo: '/'});

    }]);
})(window.angular);
