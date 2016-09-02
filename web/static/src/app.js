(function (ng) {
    var smarttoolsAPP = ng.module('smarttoolsAPP', [
        'ngRoute',
        'competitionModule',
        'webModule',
        'clientsModule',
        'videoModule'
    ]);

    smarttoolsAPP.config(['$interpolateProvider', '$routeProvider', function ($interpolateProvider, $routeProvider) {
        // configuramos los símbolos para poder llamar los {} por []
        // ya que eventualmente ponen problemas y no cargan la info del scope
        // tomado de: http://pythoniza.me/configuracion-de-angular-en-proyecto-django/

        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');


        $routeProvider
            .when('/', {
                templateUrl: '/static/src/modules/web/web.tpl.html',
                controller: 'webCtrl'
            })
            .when('/competitions', {
                templateUrl: 'static/src/modules/competitions/competition.tpl.html',
                controller: 'competitionCtrl',
                controllerAs: 'ctrl'
            })
            .when('/video', {
                templateUrl: 'static/src/modules/video/video.tpl.html',
                controller: 'videoCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise({redirectTo: '/'});

    }]);
})(window.angular);
