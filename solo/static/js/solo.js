(function() {

    marked.setOptions({
        gfm: true,
        pedantic: false,
        sanitize: false,
        highlight: function(code, lang) {
            if (lang !== undefined) {
                var highlighted = root.hljs.highlight(lang, code).value;
                return highlighted;
            } else {
                return code;
            }
        }
    });

    var root = this;


    var Solo = function(options) {

        var self = this;

        if (options && options.markdown) this.markdown = options.markdown;
        if (options && options.html) this.html = options.html;
        if (options && options.preview) this.preview = options.preview;
        if (options && options.toggleButton) this.toggleButton = options.toggleButton;
    
        this.initialize = function() {
            self.editor = root.CodeMirror.fromTextArea(self.markdown, {
                    mode: 'gfm', // github flavored markdown
                    // lineNumbers: true,
                    tabMode: "spaces",
                    matchBrackets: true,
                    theme: "solo"
            });
            self.editor.on("change", self.timeUpdate);

            this.render(); // initial render on load
            $(self.toggleButton).click(self.togglePreview);
            $(self.preview).hide();
        };

        var timer;
        this.timeUpdate = function() {
            clearTimeout(timer);
            timer = setTimeout(self.render, 500);
        };

        this.render = function() {
            self.editor.save(); // Save markdown to textarea

            var rendered = marked(self.markdown.value);
            self.html.value = rendered;
            // var toc = new TableOfContents('#toc', self.html.value ,['h1','h2','h3']);
            self.preview.innerHTML = rendered;
        };

        this.togglePreview = function() {
            $(self.preview).toggle();
            $(self.editor.getWrapperElement()).toggle();
        };

        this.initialize();

        return this;
    };

    root.Solo = Solo;

})();