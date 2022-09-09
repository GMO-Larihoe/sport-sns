<template>
    <div>
    <a id="modalOpen" class="btn btn--yellow btn--cubic" v-on:click="add">食品追加</a>
    <div id="easyModal" class="modal">
      <div class="modal-content">
        <div class="modal-header">
          <div id="newadd">
          <h1>🍚新規食品追加🍚</h1>
          </div>
          <span class="modalClose" v-on:click="close">×</span>
        </div>
        <div class="modal-body">
          <div id="E11">〇ジャンル</div>
          <div id="E12">〇食べ物</div>
          <div id="E13"><input type="file" id="uploadImage" /></div>
          <div id="E21"><input type="text" id="tansui" size="10" v-model="Wgenre"></div>
          <div id="E22"><input type="text" id="sisitu" size="10" v-model="Weat"></div>
          <div id="E23"></div>
          <div id="E14">〇炭水化物</div>
          <div id="E15">〇脂質</div>
          <div id="E16">〇タンパク質</div>
          <div id="E17">〇ミネラル</div>
          <div id="E18">〇ビタミン</div>
          <div id="E24"><input type="number" id="tansui" size="10" min="0" max="2000" v-model="Wtans"></div>
          <div id="E25"><input type="number" id="sisitu" size="10" min="0" max="2000" v-model="Wsisi"></div>
          <div id="E26"><input type="number" id="tanpaku" size="10" min="0" max="2000" v-model="Wtanp"></div>
          <div id="E27"><input type="number" id="mineraru" size="10" min="0" max="2000" v-model="Wmine"></div>
          <div id="E28"><input type="number" id="bitamin" size="10" min="0" max="2000" v-model="Wbita"></div>
          <div id="E9"><a class="btn btn--yellow2 btn--cubic" v-on:click="ok">追加！</a></div>
        </div>
      </div>
    </div>
    </div>
  </template>
  <script>
  import axios from 'axios';
  import swal from 'sweetalert';
  export default {
    name: 'ThePage1',
  
    data(){
      return{
        Wgenre : "",
        Weat : "",
        Wimg : "",
        Wtans : 1,
        Wsisi : 1,
        Wtanp : 1,
        Wmine : 1,
        Wbita : 1,
        anydata:[],
      };
   
    },
    methods: {
      add : function(){
        const modal = document.getElementById('easyModal');
        modal.style.display = 'block';
      },
      close : function(){
        const modal = document.getElementById('easyModal');
        modal.style.display = 'none';
      },
      next : async function(){
        let url = process.env.VUE_APP_API_DEV + "/users/genres";
        const API_TOKEN = sessionStorage.getItem('access_token');
        this.anydata.img=this.anydata.img.replace("data:image/png;base64,", "");
        console.log(this.anydata);
        let response = await axios.post(url, this.anydata, { headers: { Authorization: "Bearer " + API_TOKEN } });
        console.log("aaa");
        console.log(response.data);
        swal("登録完了！", "ジャンル:"+this.Wgenre+"　食べ物:"+this.Weat, "success")
        .then( () =>  { 
          this.close();
        } ) ;
      },
      ok : async function(){
        
        this.anydata={
          "genre_name" : this.Wgenre,
          "food_name" : this.Weat,
          "img" : "",
          "carbohydrate" : this.Wtans,
          "lipid" : this.Wsisi,
          "protein" : this.Wtanp,
          "mineral" : this.Wmine,
          "vitamin" : this.Wbita,
        }
        const uploadImage = document.querySelector('#uploadImage')
        const file = uploadImage.files[0]
        const reader = new FileReader()
        reader.onload = (event) => {
            this.anydata.img = event.currentTarget.result;
            this.next();
        }
        reader.readAsDataURL(file);
        
      }
    }
  }
  
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  body{
          font-family:'Noto Sans JP',sans-serif;
          background-color:#f6f5f4;
  }
  .today{
    position:absolute;
    background-color:coral;
    overflow: auto;
    width:75vw;
    height:50vh;
    margin-top:45vh;
    margin-left:20vw;
  } 
  .noweat{
    position:absolute;
    background-color: chocolate;
    width:75vw;
    height:30vh;
    margin-top:7vh;
    margin-left:20vw;
  }
  *,
  *:before,
  *:after {
    -webkit-box-sizing: inherit;
    box-sizing: inherit;
  }
  
  .btn,
  a.btn,
  button.btn {
    font-size: 1rem;
    font-weight: 700;
    line-height: 0.5;
    position: relative;
    display: inline-block;
    padding: 1rem 4rem;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-transition: all 0.3s;
    transition: all 0.3s;
    text-align: center;
    vertical-align: middle;
    text-decoration: none;
    letter-spacing: 0.1em;
    color: #212529;
    border-radius: 0.5rem;
  }
  
  a.btn--yellow {
    position: absolute;
    left:83.5vw;
    top:1vh;
    color: #000;
    background-color: #fff100;
    border-bottom: 5px solid #ccc100;
  }
  a.btn--yellow:hover {
    margin-top: 3px;
    color: #000;
    background: #fff20a;
    border-bottom: 2px solid #ccc100;
  }
  
  .modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.5);
  }
  
  .modal-content {
    background-color: #f4f4f4;
    margin: 5vh auto;
    width: 40%;
    box-shadow: 0 5px 8px 0 rgba(0,0,0,0.2),0 7px 20px 0 rgba(0,0,0,0.17);
    animation-name: modalopen;
    animation-duration: 1s;
  }
  
  @keyframes modalopen {
    from {opacity: 0}
    to {opacity: 1}
  }
  
  .modal-header h1 {
    margin: 1rem 0;
  }
  
  .modal-header {
    background: rgb(255, 223, 143);
    padding: 3px 15px;
    display: flex;
    justify-content: space-between;
  }
  
  #newadd{
    padding-left:150px;
  }
  
  .modalClose {
    font-size: 2rem;
  }
  
  .modalClose:hover {
    cursor: pointer;
  }
  
  .modal-body {
    color: black;
    display:grid;
    grid-template-rows:50px 50px 50px 50px 50px 50px 50px 50px 50px 50px 50px 25px;
    grid-template-columns:20% 30% 30%;
    background: -webkit-repeating-linear-gradient(-45deg, #f0f8ff, #f0f8ff 3px,#e9f4ff 3px, #e9f4ff 7px);
    background: repeating-linear-gradient(-45deg, #f0f8ff, #f0f8ff 3px,#e9f4ff 3px, #e9f4ff 7px);
  }
  #E11{
    grid-row: 2 / 3;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E12{
    grid-row:  3/ 4;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E13{
    grid-row:  4 / 5 ;
    grid-column: 2 / 4;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E14{
    grid-row:  5 / 6 ;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E15{
    grid-row:  6 / 7 ;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E16{
    grid-row:  7 / 8 ;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E17{
    grid-row:  8 / 9 ;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E18{
    grid-row:  9 / 10 ;
    grid-column: 2 / 3;
    background: #ffe6c3;
    border-left: solid 6px #ffb700;
  }
  #E21{
    grid-row: 2 / 3;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E22{
    grid-row:  3/ 4;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E24{
    grid-row:  5 / 6 ;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E25{
    grid-row:  6 / 7 ;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E26{
    grid-row:  7 / 8 ;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E27{
    grid-row:  8 / 9 ;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E28{
    grid-row:  9 / 10 ;
    grid-column: 3 / 4;
    background: #ffe6c3;
  }
  #E9{
    grid-row:  11 / 12 ;
    grid-column: 2 / 4;
    margin:auto;
  }
  </style>
  