$(document).ready(function(){
	
	function Project(data) {		
		var self = this;
	
		self.title = ko.observable(data.title);
		self.url = ko.observable(data.url);
	}
	
	function ProjectViewModel() {
	
		//Data
		self = this;
		self.ko_project_data = ko.observableArray([]); //Iterate through this object to fill the template
		
		self.ko_project_title = ko.observable();
		self.ko_project_url = ko.observable();		
		
		//Operations
		self.addProject = function() {
			//Do some validation before pushing the data
			var titleReg = /^\s*[a-zA-Z0-9,\s]+\s*$/;
			var urlReg = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/; 
			
			var title = this.ko_project_title();
			var url = this.ko_project_url();
			
			if(urlReg.test(url) && titleReg.test(title)) {
			
				self.ko_project_data.push(new Project({title: this.ko_project_title(), url: this.ko_project_url()}));

				//Clean up the form fields
				$('#vs-project-title').val('');
				$('#vs-project-url').val('');
				
				//Set focus to project title
				$('#vs-project-title').focus();
			}
			
			else {
				if(!titleReg.test(title))
					showalert('Invalid Project Title', 'alert-warning');
				else
					showalert('Invalid Project URL', 'alert-warning');	
			}
	
		};
			
		//Removing the projects from the list
		self.removeProject = function(project) { 
			self.ko_project_data.remove(project)			
		};
		
		//Saving the Model Data to the server
		self.saveProject = function() {
			//ToDo:
			//1. Save the model data into mysql
			//2. Redirect to the homepage
		}
	}
	
	ko.applyBindings(new ProjectViewModel());	

});

function showalert(message, alerttype) {
	$('#vs-message').text(message);
	$("#vs-alert").addClass("in");
	
	setTimeout(function() {
			$("#vs-alert").removeClass("in");
	}, 2000);
}


