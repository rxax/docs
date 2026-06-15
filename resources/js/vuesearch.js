    // Data block for search
    // Example:
    /*
    [
        {
            file: 'css_media_queries.html',
            data: 'Typical Media Query Breakpoints.'
        },
    ]
    */
    const search_data = []

    // Vue search app
    const app = Vue.createApp({
        setup(){

        },
        data() {
          return {
                search_text: localStorage.getItem("search_text") || '',
                search_results: ''
            }
        },
        methods:{
            trigger_search(event){
                // stop form submit
                event.preventDefault();
                // clear main content
                $('#static_text').empty();

                // update search field
                localStorage.setItem("search_text", this.search_text)
                // do search
                this.search_results = '<h4>Results for <span class="fst-italic">'+this.search_text+'</span></h4>';
                const results = fuzzysort.go(this.search_text, search_data, {key: 'data'})


                if(results.length === 0){
                    this.search_results+= 'No matching results found.'
                    return
                    }

                // filter results for better score
                const filtered_results = results.filter(val => val.score>0.35);
                if (filtered_results.length === 0) {
                    this.search_results+= 'No matching results found.'
                } else {
                    this.search_results+= '<div class="row">'

                    for(result of filtered_results){
                       this.search_results+=`<p><a href="${result.obj.file}">${result.obj.file}</a>${result.score}</p>`
                    }
                    this.search_results+='</div>'
                }




            }
        }
  });

  //Ignore sidebar tag
  app.config.compilerOptions.isCustomElement = (tag) => {
                return tag === 'sidebar' || tag === 'code'
  }

  app.mount('#vue_app')