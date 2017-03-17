
var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('studentHomeCtrl', function($scope, $http) {

    $scope.quiz_list_url = '/quiz/api/activequizes/';
    $scope.quizList = function () {
	            
	            $http.get($scope.quiz_list_url, { cache: true }).success(function (data) {
	                $scope.quizListData=data.results;
	                });
	               
    };
    $scope.quizList();         
});


app.controller('quizDetailsCtrl', function($scope, $http) {
        $scope.init = function (quiz_id) {
            console.log(quiz_id);
            $http.get('/quiz/api/quizes/' + quiz_id, { cache: true }).success(function (data) {
            	$scope.quizDetails= data;
                console.log("data",$scope.quizDetails)
                });
            };
});


app.controller('quizProgressCtrl', function($scope, $http) {
        $scope.init = function (quiz_id) {
            console.log(quiz_id);
            $http.get('/quiz/api/quiz/' + quiz_id, { cache: true }).success(function (data) {
	                    $scope.questions=data.results;      
                });
            };
});