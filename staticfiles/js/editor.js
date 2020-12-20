var Preview = {
  delay: 50,        // delay after keystroke before updating

  preview: null,     // filled in by Init below
  buffer: null,      // filled in by Init below

  timeout: null,     // store setTimout id
  mjRunning: false,  // true when MathJax is processing
  oldText: null,     // used to check if an update is needed

  //
  //  Get the preview and buffer DIV's
  //
  Init: function () {
    this.preview = document.getElementById("pergunta_preview");
    this.buffer = document.getElementById("pergunta_buffer");
  },

  //
  //  Switch the buffer and preview, and display the right one.
  //  (We use visibility:hidden rather than display:none since
  //  the results of running MathJax are more accurate that way.)
  //
  SwapBuffers: function () {
    var buffer = this.preview, preview = this.buffer;
   // this.buffer = buffer; this.preview = preview;
    buffer.style.visibility = "hidden"; buffer.style.position = "absolute";
    preview.style.position = ""; preview.style.visibility = "";
  },

  //
  //  This gets called when a key is pressed in the textarea.
  //  We check if there is already a pending update and clear it if so.
  //  Then set up an update to occur after a small delay (so if more keys
  //    are pressed, the update won't occur until after there has been 
  //    a pause in the typing).
  //  The callback function is set up below, after the Preview object is set up.
  //
  Update: function () {
    if (this.timeout) {clearTimeout(this.timeout)}
    this.timeout = setTimeout(this.callback,this.delay);
  },

  //
  //  Creates the preview and runs MathJax on it.
  //  If MathJax is already trying to render the code, return
  //  If the text hasn't changed, return
  //  Otherwise, indicate that MathJax is running, and start the
  //    typesetting.  After it is done, call PreviewDone.
  //  
  CreatePreview: function () {
    Preview.timeout = null;
    if (this.mjRunning) return;

      // verifica se há uma imagem

    if (BQ.Storage.Get({key:'upload_upload'}) !== null) {

      var text2 = document.getElementById("pergunta").value;
      var text = '<center><img style="width: 8cm" src="'+BQ.Storage.Get({key:'upload_upload'})+'" /></center><br /><br />' + text2;

    } else {

      var text = document.getElementById("pergunta").value;
      
    }

    if (text === this.oldtext) return;
    this.buffer.innerHTML = this.oldtext = text;
    this.mjRunning = true;
    MathJax.Hub.Queue(
      ["Typeset",MathJax.Hub,this.buffer],
      ["PreviewDone",this]
    );
  },

  //
  //  Indicate that MathJax is no longer running,
  //  and swap the buffers to show the results.
  //
  PreviewDone: function () {
    this.mjRunning = false;
    this.SwapBuffers();
  }

};

//
//  Cache a callback to the CreatePreview action
//
Preview.callback = MathJax.Callback(["CreatePreview",Preview]);
Preview.callback.autoReset = true;  // make sure it can run more than once




var PreviewAnswer = {
  delay: 50,        // delay after keystroke before updating

  PreviewAnswer: null,     // filled in by Init below
  buffer: null,      // filled in by Init below

  timeout: null,     // store setTimout id
  mjRunning: false,  // true when MathJax is processing
  oldText: null,     // used to check if an update is needed

  //
  //  Get the PreviewAnswer and buffer DIV's
  //
  Init: function () {
    this.PreviewAnswer = document.getElementById("resposta_preview");
    this.buffer = document.getElementById("resposta_buffer");
  },

  //
  //  Switch the buffer and PreviewAnswer, and display the right one.
  //  (We use visibility:hidden rather than display:none since
  //  the results of running MathJax are more accurate that way.)
  //
  SwapBuffers: function () {
    var buffer = this.PreviewAnswer, PreviewAnswer = this.buffer;
   // this.buffer = buffer; this.PreviewAnswer = PreviewAnswer;
    buffer.style.visibility = "hidden"; buffer.style.position = "absolute";
    PreviewAnswer.style.position = ""; PreviewAnswer.style.visibility = "";
  },

  //
  //  This gets called when a key is pressed in the textarea.
  //  We check if there is already a pending update and clear it if so.
  //  Then set up an update to occur after a small delay (so if more keys
  //    are pressed, the update won't occur until after there has been 
  //    a pause in the typing).
  //  The callback function is set up below, after the PreviewAnswer object is set up.
  //
  Update: function () {
    if (this.timeout) {clearTimeout(this.timeout)}
    this.timeout = setTimeout(this.callback,this.delay);
  },

  //
  //  Creates the PreviewAnswer and runs MathJax on it.
  //  If MathJax is already trying to render the code, return
  //  If the text hasn't changed, return
  //  Otherwise, indicate that MathJax is running, and start the
  //    typesetting.  After it is done, call PreviewAnswerDone.
  //  
  CreatePreviewAnswer: function () {
    PreviewAnswer.timeout = null;
    if (this.mjRunning) return;

      // verifica se há uma imagem

 
     var text = document.getElementById("resposta").value;
 
        

    if (text === this.oldtext) return;
    this.buffer.innerHTML = this.oldtext = text;
    this.mjRunning = true;
    MathJax.Hub.Queue(
      ["Typeset",MathJax.Hub,this.buffer],
      ["PreviewAnswerDone",this]
    );
  },

  //
  //  Indicate that MathJax is no longer running,
  //  and swap the buffers to show the results.
  //
  PreviewAnswerDone: function () {
    this.mjRunning = false;
    this.SwapBuffers();
  }

};

//
//  Cache a callback to the CreatePreviewAnswer action
//
PreviewAnswer.callback = MathJax.Callback(["CreatePreviewAnswer",PreviewAnswer]);
PreviewAnswer.callback.autoReset = true;  // make sure it can run more than once



