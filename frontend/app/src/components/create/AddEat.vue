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
          <div id="eat">
          <div id="E11">ジャンル</div>
          <div id="E12">食べ物</div>
          <div id="E21"><input type="text" id="tansui" size="10" v-model="Wgenre"></div>
          <div id="E22"><input type="text" id="sisitu" size="10" v-model="Weat"></div>
          </div>
          <input type="file" id="uploadImage" />
          <div id="godai">
          <div id="G11">〇炭水化物</div>
          <div id="G12">〇脂質</div>
          <div id="G13">〇タンパク質</div>
          <div id="G14">〇ミネラル</div>
          <div id="G15">〇ビタミン</div>
          <div id="G21"><input type="number" id="tansui" size="10" min="0" max="2000" v-model="Wtans"></div>
          <div id="G22"><input type="number" id="sisitu" size="10" min="0" max="2000" v-model="Wsisi"></div>
          <div id="G23"><input type="number" id="tanpaku" size="10" min="0" max="2000" v-model="Wtanp"></div>
          <div id="G24"><input type="number" id="mineraru" size="10" min="0" max="2000" v-model="Wmine"></div>
          <div id="G25"><input type="number" id="bitamin" size="10" min="0" max="2000" v-model="Wbita"></div>
          </div>
          <a class="btn btn--yellow2 btn--cubic" v-on:click="ok">追加！</a>
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
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
  #ttext{
    position:absolute;
    font-size:120%;
    width:auto;
    height:auto;
    background-color:chartreuse;
    margin-top:40vh;
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
  a.btn--yellow2 {
    color: #000;
    background-color: #fff100;
    border-bottom: 5px solid #ccc100;
  }
  a.btn--yellow2:hover {
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
    margin: 10vh auto;
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
    background: lightblue;
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
    padding: 50px 200px;
    color: black;
    display:grid;
  }
  
  #eat{
    display:grid;
    grid-template-rows:60px 60px ;
    grid-template-columns:80px 200px;
      font-size:120%;
  }
  #E11 {
      grid-row: 1 / 2;
      grid-column: 1 / 2;
      background: #f88;
      padding-top:20%;
  }
  #E12 {
      grid-row: 2 / 3;
      grid-column: 1 / 2;
      background: #8f8;
      padding-top:20%;
  }
  #E21 {
      text-align: center;
      grid-row: 1 / 2;
      grid-column: 2 / 3;
      background: #f88;
  }
  #E22 {
      text-align: center;
      grid-row: 2 / 3;
      grid-column: 2 / 3;
      background: #8f8;
  }
  
  #godai{
    display:grid;
    grid-template-rows:30px 30px 30px 30px 30px;
    grid-template-columns:100px 100px;
  }
  #G11 {
      grid-row: 1 / 2;
      grid-column: 1 / 2;
      background: #f88;
  }
  #G12 {
      grid-row: 2 / 3;
      grid-column: 1 / 2;
      background: #8f8;
  }
  #G13 {
      grid-row: 3 / 4;
      grid-column: 1 / 2;
      background: #88f;
  }
  #G14 {
      grid-row: 4 / 5;
      grid-column: 1 / 2;
      background: #8f8;
  }
  #G15 {
      grid-row: 5 / 6;
      grid-column: 1 / 2;
      background: #f88;
  }
  #G21 {
      text-align: center;
      grid-row: 1 / 2;
      grid-column: 2 / 3;
      background: #f88;
  }
  #G22 {
      text-align: center;
      grid-row: 2 / 3;
      grid-column: 2 / 3;
      background: #8f8;
  }
  #G23 {
      text-align: center;
      grid-row: 3 / 4;
      grid-column: 2 / 3;
      background: #88f;
  }
  #G24 {
      text-align: center;
      grid-row: 4 / 5;
      grid-column: 2 / 3;
      background: #8f8;
  }
  #G25 {
      text-align: center;
      grid-row: 5 / 6;
      grid-column: 2 / 3;
      background: #f88;
  }
  </style>
  