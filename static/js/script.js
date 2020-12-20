/*
 *  IR Script
 */
 "use strict";

 try {

    var Sys = {

        Info: {

            Version: function() {
                return ("1.0.2")
            }

        },

        Redirect:function (url) {
          location.href = url;
        },

        Open:function (url) {
          window.open(url, '_blank')
        },

        Cookie: {
            Delete:function(json){
                if (json !== undefined) {
                    if (typeof json == "object") {

                        if (json.name == undefined || json.name == "") {
                            throw new Error('System.Cookie.Delete({name:""});');
                        }

                        try {
                            System.Cookie.Set({name:json.name, value:"", exdays:"-1"})
                        } catch (e) {
                            throw new Error('System.Cookie.Set({name:"", value:"", exdays:"1"});');
                        }
                    }
                }
            },

            Set:function(json){

                if (json !== undefined) {
                    if (typeof json == "object") {

                        if (json.name == undefined || json.name == "") {
                            throw new Error('System.Cookie.Set({name:"", value:"", exdays:"1"});');
                        }

                        if (json.value == undefined) {
                           json.value = "";
                        }

                        if (json.exdays == undefined) {
                           json.exdays = 1;
                        }

                        try {
                            var d = new Date();
                            d.setTime(d.getTime() + (json.exdays * 24 * 60 * 60 * 1000));
                            var expires = "expires="+d.toUTCString();
                            document.cookie = json.name + "=" + json.value + ";" + expires + ";path=/";
                        } catch (e) {
                            throw new Error('System.Cookie.Set({name:"", value:"", exdays:"1"});');
                        }
                    }
                }


            },

            Get:function(json){

                if (json !== undefined) {
                    if (typeof json == "object") {
                        if (json.name == undefined) {
                            return "";
                        } else {
                            var name = json.name + "=";
                            var ca = document.cookie.split(';');

                            for(var i = 0; i < ca.length; i++) {
                                var c = ca[i];
                                while (c.charAt(0) == ' ') {
                                    c = c.substring(1);
                                }

                                if (c.indexOf(name) == 0) {
                                    return c.substring(name.length, c.length);
                                }
                            }
                            return "";
                        }
                    }
                }
            }
        },
        
        Ajax: {

            Get: function(json) {

                if (json !== undefined) {

                    if (typeof json == "object") {

                        // Checks if the parameter was passed.
                        if (json.url == undefined) {
                            json.url = "/";
                        }

                        // Checks if the parameter was passed.
                        if (json.data == undefined) {
                            json.data = "";
                        }

                        // Checks if the parameter was passed.
                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.first == undefined) {
                            json.first = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        if (json.last == undefined) {
                            json.last = function() {};
                        }

                        json.first();

                        try {
                            var get = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var get = new ActiveXObject("Msxml2.XMLHTTP");
                            } catch (b) {
                                try {
                                    var get = new ActiveXObject("Microsoft.XMLHTTP");
                                } catch (c) {
                                    var get = false;
                                }
                            }
                        }

                        // Send request.
                        get.open("GET", json.url + "?" + json.data, true);
                        // Builds a scan input.
                        get.onreadystatechange = function() {

                            if(document.getElementById("progress")) {
                                 switch (this.readyState) {
                                    case 0:
                                    document.getElementById("progress").value = "0";
                                    break;
                                    case 1:
                                    document.getElementById("progress").value = "25";
                                    break;
                                    case 2:
                                    document.getElementById("progress").value = "50";
                                    break;
                                    case 3:
                                    document.getElementById("progress").value = "75";
                                    break;
                                    case 4:
                                    document.getElementById("progress").value = "100";

                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                        json.last();
                                        document.getElementById("progress").value = "0";

                                    } else {
                                        json.error();
                                        document.getElementById("progress").value = "0";
                                    }

                                    break;
                                }
                            } else {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                        json.last();
                                    } else {
                                        json.error();
                                    }
                                }
                            }
                        }

                        get.send(null);
                        console.log("System.Ajax.Get()");

                    } else {
                        throw new Error('System.Ajax.Get({url:"", data:"", first:function(){}, success:function(){}, last:function(){}, error:function(){}});');
                    }

                } else {

                    throw new Error('System.Ajax.Get({url:"", data:"", first:function(){}, success:function(){}, last:function(){}, error:function(){}});');
                }

            },

            Post: function(json) {

                if (json !== undefined) {

                    if (typeof json == "object") {

                        // Checks if the parameter was passed.
                        if (json.url == undefined) {
                            json.url = "/";
                        }

                        // Checks if the parameter was passed.
                        if (json.data == undefined) {
                            json.data = "";
                        }

                        // Checks if the parameter was passed.
                        if (json.success == undefined) {
                            json.success = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.first == undefined) {
                            json.first = function() {};
                        }

                        // Checks if the parameter was passed.
                        if (json.error == undefined) {
                            json.error = function() {};
                        }

                        if (json.last == undefined) {
                            json.last = function() {};
                        }

                        json.first();

                        // Identifies which browser and load base files.
                        try {
                            var post = new XMLHttpRequest();
                        } catch (a) {
                            try {
                                var post = new ActiveXObject("Msxml2.XMLHTTP");
                            } catch (b) {
                                try {
                                    var post = new ActiveXObject("Microsoft.XMLHTTP");
                                } catch (c) {
                                    var post = false;
                                }
                            }
                        }

                        // Builds a scan input.
                        post.onreadystatechange = function() {
                            if(document.getElementById("progress")) {
                                 switch (this.readyState) {
                                    case 0:
                                    document.getElementById("progress").value = "0";
                                    break;
                                    case 1:
                                    document.getElementById("progress").value = "25";
                                    break;
                                    case 2:
                                    document.getElementById("progress").value = "50";
                                    break;
                                    case 3:
                                    document.getElementById("progress").value = "75";
                                    break;
                                    case 4:
                                    document.getElementById("progress").value = "100";

                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                        json.last();
                                        document.getElementById("progress").value = "0";
                                         
                                    } else {
                                        json.error();
                                        document.getElementById("progress").value = "0";
                                    }

                                    break;
                                }
                            } else {
                                if (this.readyState === 4) {
                                    if (this.status >= 200 && this.status < 299) {
                                        var resp = this.responseText;
                                        json.success(resp);
                                        json.last();
                                    } else {
                                        json.error();
                                    }
                                }
                            }
                        }
                        // Send request.
                        post.open('POST', json.url, true);
                        post.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                        post.send(json.data);

                        console.log("System.Ajax.Post()");

                    } else {
                        throw new Error('System.Ajax.Post({url:"", data:"", first:function(){}, success:function(){}, last:function(){}, error:function(){}});');
                    }

                } else {
                    throw new Error('System.Ajax.Post({url:"", data:"", first:function(){}, success:function(){}, last:function(){}, error:function(){}});');
                }
            }

        }

    };

    var System = Object.create(Sys);

} catch (e) {

    throw new Error(e);

} finally {

    console.log("IR Script " + System.Info.Version() + " Started");

}


// Tutorial Script, depende do IR Script
try {

    var T = {

        Info: {

            Version: function() {
                return ("1.0.0")
            }

        },

        Get:function (json) {
          if (json !== undefined) {
              if (typeof json == "object") {

                  if (json.name == undefined || json.name == "") {
                      throw new Error('Tutorial.Get({name:"início"});');
                  }
                  // verifica se o tutorial de json.name já foi rodado
                  var k=0;
                  var i = System.Cookie.Get({name:"tutorial"}).split(",");
                  for (var j = 0; j < i.length; j++) {
                      if (i[j] == json.name) {
                        k=k+1;
                      }
                  }
                  if (k==1) {
                    //json.name encontrado
                    return true;
                  } else {
                    //json.name não encontrado
                    return false;
                  }
                  
              }
          }
        },

        Set:function(json){

            if (json !== undefined) {
                if (typeof json == "object") {
                    if (json.name == undefined || json.name == "") {
                        throw new Error('Tutorial.Set({name:"início"});');
                    }
                    if (System.Cookie.Get({name:"tutorial"}) == "") {
                        System.Cookie.Set({
                            name:"tutorial", 
                            value:"[]"
                        });
                        var tutorial = [];
                    } else {
                        var tutorial = [];
                        var i = System.Cookie.Get({name:"tutorial"}).split(",");
                        for (var j = 0; j < i.length; j++) {
                            if (!tutorial.includes(i[j])) {
                                tutorial.push(i[j]);                      
                            }
                        }
                    }
                    if (!tutorial.includes(json.name)) {
                        tutorial.push(json.name);
                        System.Cookie.Set({
                            name:"tutorial", 
                            value:tutorial,
                            exdays:"30"
                        });
                    }
                }
            }
        },
    };

    var Tutorial = Object.create(T);

} catch (e) {

    throw new Error(e);

} finally {

    console.log("Tutorial Script " + Tutorial.Info.Version() + " Started");

}