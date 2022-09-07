<template>
    <div class="m-5 text-center">
      <!-- メールアドレス -->
      <div class="m-1">
        <input type="email" v-model="email" placeholder="メール">
      </div>
  
      <!-- パスワード -->
      <div class="m-1">
        <input type="password" v-model="password" placeholder="パスワード">
      </div>
  
      <!-- ログインボタン -->
      <div class="m-3">
        <button class="btn btn-primary" @click="login">ログイン</button>
      </div>
  
      <!-- 新規登録 -->
      <div class="m-1">
          <a href="/provisional_signup">新規登録</a>
      </div>
    </div>
  </template>

<script>

import axios from 'axios'; 
import router from './router/router.js'
export default {
    data() {
        return {
        email: "",
        password: "",
        };
    },
    setup(){
        
    },
    mounted() {
        

    },
    methods: {
        login: async function(){
            const params = new URLSearchParams();
            params.append('username', this.email);    // 渡したいデータ分だけappendする
            params.append('password', this.password);
            let config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            };
            let url = process.env.VUE_APP_API_DEV + '/token';
            const response = await axios.post(url, params, config);
            console.log("response.data = ", response.data)
            sessionStorage.setItem('access_token', response.data.access_token);
            router.push('/home')
        },
        
    },
}
</script>