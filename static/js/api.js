'use strict';

try {

    let BQSys = {

        Info: {

            Version: function() {
                return ('v1');
            },

            Url: function() {
            	if (location.hostname === "192.168.0.100"){
            		return ('http://192.168.0.100:8000/api/');
            	} else {
	            	if (location.hostname === "localhost" || location.hostname === "127.0.0.1"){
	            		return ('http://localhost:8000/api/');
	            	} else {
	            		return ('https://bq.mat.br/api/');
	            	}
            	}

 
            }

        },

        Storage: {

        	Set: function(json){

                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.key !== undefined) {
	 
	                        if (json.value == undefined) {
	                            json.value = '';
	                        }

	                        return sessionStorage.setItem(json.key, json.value.toString());
                        }
                     }
                }
        	},
 

        	Get: function(json){

                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.key !== undefined) {
	                        
	                        return sessionStorage.getItem(json.key) || null;
                        }
                    }
                }
        	},

        	Remove: function(json){

                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.key !== undefined) {
	                        
	                        return sessionStorage.removeItem(json.key);

                        } else {

                        	return sessionStorage.clear();
                        }
                    }
                }
        	}
        },

        Api: {

	        CreateStorageAll: function(json){

	            if (json !== undefined) {

	                if (typeof json == 'object') {

	                    if (json.token == undefined) {
	                        json.token = '';
	                    }


						BQ.Api.CreateStorage({
							token:json.token,
							route:'etapa',
						});

						BQ.Api.CreateStorage({
							token:json.token,
							route:'niveldedificuldade',
						});

						BQ.Api.CreateStorage({
							token:json.token,
							route:'unidadetematica',
						});


						BQ.Api.CreateStorage({
							token:json.token,
							route:'objetodeconhecimento',
						});

	                }
	            }
	        },

	        CreateStorage: function(json){

	            if (json !== undefined) {

	                if (typeof json == 'object') {

	                    if (json.route == undefined) {
	                        json.route = '';
	                    }

	                    if (json.token == undefined) {
	                        json.token = '';
	                    }

	                    if (json.route == 'etapa') {

	                    	json.route = json.route + '/';

							BQ.Api.Get({

								token:json.token,
								route:json.route,
								success:function(rtn){
									var json_ = JSON.parse(rtn);
									
									if (json_.next == null) {

										for (var i = 0; i < json_.results.length; i++) {

											BQ.Storage.Set({
												key:'etapa_'+json_.results[i].etapa,
												value:json_.results[i].etapa_nome
											});

										}
										
									} else {

										var j = Math.round(json_.count/10);

										for (var k = 1; k < (j+1);) {

											BQ.Api.Get({
												token:json.token,
												route:json.route,
												uri:'page='+k,
												success:function(rtn){
													var json__ = JSON.parse(rtn);
													for (var i = 0; i < json__.results.length; i++) {
														BQ.Storage.Set({
															key:'etapa_'+json_.results[i].etapa,
															value:json_.results[i].etapa_nome
														});
													}
												}
											});

											k++;
										}
									}
								}
							});

	                    } else { if (json.route == 'unidadetematica') {

	                    	json.route = json.route + '/';

							BQ.Api.Get({
								token:json.token,
								route:json.route,
								success:function(rtn){
									var json_ = JSON.parse(rtn);
									
									if (json_.next == null) {

										for (var i = 0; i < json_.results.length; i++) {

											BQ.Storage.Set({
												key:'unidade_tematica_'+json_.results[i].unidade_tematica+'_etapa', 
												value:json_.results[i].etapa
											});

											BQ.Storage.Set({
												key:'unidade_tematica_'+json_.results[i].unidade_tematica+'_ano',
												value:json_.results[i].ano
											});

											BQ.Storage.Set({
												key:'unidade_tematica_'+json_.results[i].unidade_tematica+'_nome', 
												value:json_.results[i].unidade_tematica_nome
											});

										}
										
									} else {

										var j = Math.round(json_.count/10);

										for (var k = 1; k < (j+1);) {

											BQ.Api.Get({
												token:json.token,
												route:json.route,
												uri:'page='+k,
												success:function(rtn){
													var json__ = JSON.parse(rtn);
													for (var i = 0; i < json__.results.length; i++) {
														BQ.Storage.Set({
															key:'unidade_tematica_'+json__.results[i].unidade_tematica+'_etapa', 
															value:json__.results[i].etapa
														});

														BQ.Storage.Set({
															key:'unidade_tematica_'+json__.results[i].unidade_tematica+'_ano',
															value:json__.results[i].ano
														});

														BQ.Storage.Set({
															key:'unidade_tematica_'+json__.results[i].unidade_tematica+'_nome', 
															value:json__.results[i].unidade_tematica_nome
														});
													}
												}
											});

											k++;
										}
									}
								}
							});

	                    } else { if (json.route == 'objetodeconhecimento') {
	                    	json.route = json.route + '/';

							BQ.Api.Get({
								token:json.token,
								route:json.route,
								success:function(rtn){
									var json_ = JSON.parse(rtn);
									
									if (json_.next == null) {

										for (var i = 0; i < json_.results.length; i++) {

											BQ.Storage.Set({
												key:'objeto_de_conhecimento_'+json_.results[i].objeto_de_conhecimento+'_etapa', 
												value:json_.results[i].etapa
											});

											BQ.Storage.Set({
												key:'objeto_de_conhecimento_'+json_.results[i].objeto_de_conhecimento+'_ano',
												value:json_.results[i].ano
											});

											BQ.Storage.Set({
												key:'objeto_de_conhecimento_'+json_.results[i].objeto_de_conhecimento+'_unidade_tematica',
												value:json_.results[i].unidade_tematica
											});


											BQ.Storage.Set({
												key:'objeto_de_conhecimento_'+json_.results[i].objeto_de_conhecimento+'_nome', 
												value:json_.results[i].objeto_de_conhecimento_nome
											});

										}
										
									} else {

										var j = Math.round(json_.count/10);

										for (var k = 1; k < (j+1);) {

											BQ.Api.Get({
												token:json.token,
												route:json.route,
												uri:'page='+k,
												success:function(rtn){
													var json__ = JSON.parse(rtn);
													for (var i = 0; i < json__.results.length; i++) {
														BQ.Storage.Set({
															key:'objeto_de_conhecimento_'+json__.results[i].objeto_de_conhecimento+'_etapa', 
															value:json__.results[i].etapa
														});

														BQ.Storage.Set({
															key:'objeto_de_conhecimento_'+json__.results[i].objeto_de_conhecimento+'_ano',
															value:json__.results[i].ano
														});

														BQ.Storage.Set({
															key:'objeto_de_conhecimento_'+json__.results[i].objeto_de_conhecimento+'_unidade_tematica',
															value:json__.results[i].unidade_tematica
														});


														BQ.Storage.Set({
															key:'objeto_de_conhecimento_'+json__.results[i].objeto_de_conhecimento+'_nome', 
															value:json__.results[i].objeto_de_conhecimento_nome
														});

													}
												}
											});

											k++;
										}
									}
								}
							});

	                    } else {if (json.route == 'niveldedificuldade') {

	                    	json.route = json.route + '/';


							BQ.Api.Get({

								token:json.token,
								route:json.route,
								success:function(rtn){
									var json_ = JSON.parse(rtn);
									
									if (json_.next == null) {

										for (var i = 0; i < json_.results.length; i++) {

											BQ.Storage.Set({
												key:'nivel_de_dificuldade_'+json_.results[i].nivel_de_dificuldade,
												value:json_.results[i].nivel_de_dificuldade_nome
											});

										}
										
									} else {

										var j = Math.round(json_.count/10);

										for (var k = 1; k < (j+1);) {

											BQ.Api.Get({
												token:json.token,
												route:json.route,
												uri:'page='+k,
												success:function(rtn){
													var json__ = JSON.parse(rtn);
													for (var i = 0; i < json__.results.length; i++) {
														BQ.Storage.Set({
															key:'nivel_de_dificuldade_'+json__.results[i].nivel_de_dificuldade,
															value:json__.results[i].nivel_de_dificuldade_nome
														});
													}
												}
											});

											k++;
										}
									}
								}
							});

	                    }}}}
	                }
	            }
	        },

        	Get: function(json){

                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.version == undefined) {
                            json.version = BQ.Info.Version();
                        }

                        if (json.route == undefined) {
                            json.route = '';
                        }

                        if (json.url == undefined) {
                            json.url = null;
                        }

                        if (json.data == undefined) {
                            json.data = '';
                        } else {
                        	 
                        	var uri = Object.keys(json.data).map(
                        		function(k) { 
                        			return encodeURIComponent(k) + '=' + encodeURIComponent(json.data[k])
                        		}).join('&');

                        	json.data = uri;

                        	 
                        }

                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        if (json.error == undefined) {
                            json.error = function() {};
                        }


                        try {
                            var Get = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var Get = new ActiveXObject('Msxml2.XMLHTTP');
                            } catch (b) {
                                try {
                                    var Get = new ActiveXObject('Microsoft.XMLHTTP');
                                } catch (c) {
                                    var Get = false;
                                }
                            }
                        }

                        if (Get) {

                        	if (json.url == null) {

		                        if (json.id == undefined) {
	                        		Get.open('GET', BQ.Info.Url() + json.version + '/' + json.route + '?format=json&' + json.data , true);
		                        } else {
		                        	Get.open('GET', BQ.Info.Url() + json.version + '/' + json.route + json.id + '/' + '?format=json&' + json.data, true);
		                        }

                        	} else {
	                        	
	                        	Get.open('GET', json.url, true);

                        	}

	                        if (json.headers !== undefined) {
	                        	
							  for (var key in json.headers) {
							      if (json.headers.hasOwnProperty(key)) {
							          Get.setRequestHeader(key,json.headers[key]);
							      }
							  }
	                        }

	                        Get.onload = function() {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                   }  else {
                                    	var resp = this.responseText;
                                        json.error(resp);
                                    }
                                }  
	                        }
                        	 
	                        Get.send(null);
	                        console.log('BQ.Api.Get()');

                        } else {

                        	
                        }

                    } else {
                    	
                    }

                } else {
                	
                }
        	},

        	Delete: function(json){
                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.version == undefined) {
                            json.version = BQ.Info.Version();
                        }

                        if (json.route == undefined) {
                            json.route = '';
                        }

                        if (json.id == undefined) {
                            json.id = -1;
                        }

                        if (json.success == undefined) {
                            json.success = function() {};
                        }


                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        try {
                            var Delete = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var Delete = new ActiveXObject('Msxml2.XMLHTTP');
                            } catch (b) {
                                try {
                                    var Delete = new ActiveXObject('Microsoft.XMLHTTP');
                                } catch (c) {
                                    var Delete = false;
                                }
                            }
                        }

                        if (Delete) {

                        	Delete.open('DELETE', BQ.Info.Url() + json.version + '/' + json.route + json.id + '/', true);

	                        if (json.headers !== undefined) {
	                        	
							  for (var key in json.headers) {
							      if (json.headers.hasOwnProperty(key)) {
							          Delete.setRequestHeader(key,json.headers[key]);
							      }
							  }
	                        }

	                        Delete.onload = function() {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                    }  else {
                                    	var resp = this.responseText;
                                        json.error(resp);
                                    }
                                }
	                        }
                        	 
	                        Delete.send(null);

	                        console.log('BQ.Api.Delete()');
                        }
                    }
            	}
        	},

         	Put: function(json){
                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.version == undefined) {
                            json.version = BQ.Info.Version();
                        }

                        if (json.route == undefined) {
                            json.route = '';
                        }

                        if (json.id == undefined) {
                            json.id = -1;
                        }

                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        try {
                            var Put = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var Put = new ActiveXObject('Msxml2.XMLHTTP');
                            } catch (b) {
                                try {
                                    var Put = new ActiveXObject('Microsoft.XMLHTTP');
                                } catch (c) {
                                    var Put = false;
                                }
                            }
                        }

                        if (Put) {

                        	Put.open('PUT', BQ.Info.Url() + json.version + '/' + json.route + json.id + '/', true);

	                        if (json.headers !== undefined) {
	                        	
							  for (var key in json.headers) {
							      if (json.headers.hasOwnProperty(key)) {
							          Put.setRequestHeader(key,json.headers[key]);
							      }
							  }
	                        }


	                        var data = new FormData();

	                        if (json.data !== undefined) {

							  for (var key in json.data) {

							      if (json.data.hasOwnProperty(key)) {
							      	data.append(key, json.data[key]);
							      }
							  }
	                        }


	                        Put.onload = function() {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                    }  else {
                                    	var resp = this.responseText;
                                        json.error(resp);
                                    }
                                }
	                        }
                        	 
	                        Put.send(data);
	                        console.log('BQ.Api.Put()');
                        }
                    }
            	}
        	},

         	Patch: function(json){
                if (json !== undefined) {

                    if (typeof json == 'object') {

                        if (json.version == undefined) {
                            json.version = BQ.Info.Version();
                        }

                        if (json.route == undefined) {
                            json.route = '';
                        }

                        if (json.id == undefined) {
                            json.id = -1;
                        }

                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        try {
                            var Patch = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var Patch = new ActiveXObject('Msxml2.XMLHTTP');
                            } catch (b) {
                                try {
                                    var Patch = new ActiveXObject('Microsoft.XMLHTTP');
                                } catch (c) {
                                    var Patch = false;
                                }
                            }
                        }

                        if (Patch) {

                        	Patch.open('PATCH', BQ.Info.Url() + json.version + '/' + json.route + json.id + '/', true);
	                       
	                        if (json.headers !== undefined) {
	                        	
							  for (var key in json.headers) {
							      if (json.headers.hasOwnProperty(key)) {
							          Patch.setRequestHeader(key,json.headers[key]);
							      }
							  }
	                        }

	                        var data = new FormData();

	                        if (json.data !== undefined) {

							  for (var key in json.data) {

							      if (json.data.hasOwnProperty(key)) {
							      	data.append(key, json.data[key]);
							      }
							  }
	                        }


	                        Patch.onload = function() {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                    }  else {
                                    	var resp = this.responseText;
                                        json.error(resp);
                                    }
                                }
	                        }
                        	 
	                        Patch.send(data);
	                        console.log('BQ.Api.Patch()');
                        }
                    }
            	}
        	},

         	Post: function(json){
                if (json !== undefined) {

                    if (typeof json == 'object') {
 
                        if (json.version == undefined) {
                            json.version = BQ.Info.Version();
                        }

                        if (json.route == undefined) {
                            json.route = '';
                        }

                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        try {
                            var Post = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var Post = new ActiveXObject('Msxml2.XMLHTTP');
                            } catch (b) {
                                try {
                                    var Post = new ActiveXObject('Microsoft.XMLHTTP');
                                } catch (c) {
                                    var Post = false;
                                }
                            }
                        }

                        if (Post) {

                        	Post.open('POST', BQ.Info.Url() + json.version + '/' + json.route, true);

	                        if (json.headers !== undefined) {
	                        	
							  for (var key in json.headers) {
							      if (json.headers.hasOwnProperty(key)) {
							          Post.setRequestHeader(key,json.headers[key]);
							      }
							  }
	                        }

	                        var data = new FormData();

	                        if (json.data !== undefined) {

							  for (var key in json.data) {

							      if (json.data.hasOwnProperty(key)) {
							      	data.append(key, json.data[key]);
							      }
							  }
	                        }

	                        Post.onload = function() {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                    }  else {
                                    	var resp = this.responseText;
                                        json.error(resp);
                                    }
                                }
	                        }
                        	
                        	Post.send(data);

	                        console.log('BQ.Api.Post()');
                        }
                    }
            	}
        	},
        }
    };

    var BQ = Object.create(BQSys);

} catch (e) {

    throw new Error(e);

} finally {

    console.log('BQ JS API ' + BQ.Info.Version() + ' Started');

}