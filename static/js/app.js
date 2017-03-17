
var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('studentHomeCtrl', function($scope, $http) {
    $scope.quizListData = [];
    $scope.quiz_list_url = '/quiz/api/activequizes/';
    $scope.quizList = function () {
	            
	            $http.get($scope.quiz_list_url, { cache: true }).success(function (data) {
	                angular.forEach(data.results, function (item) {
	                    $scope.quizListData.push(item);
	                    
	                });
	                });
	               console.log("data",$scope.quizListData)
    };
    $scope.quizList();         
});


app.controller('quizDetailsCtrl', function($scope, $http) {
		$scope.quizDetailss=[];
        $scope.init = function (quiz_id) {
            console.log(quiz_id);
            $http.get('/quiz/api/activequizes/' + quiz_id, { cache: true }).success(function (data) {
            	$scope.quizDetails= data;
                console.log("data",$scope.quizDetails)
                });
            };
});
