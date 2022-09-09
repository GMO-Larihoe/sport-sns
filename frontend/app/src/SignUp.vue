<template>
    <div class="m-5 text-center">
      <p class="m-1">氏名を入力してください。</p>
      <!-- 名前 -->
      <div class="m-1">
        <input type="text" v-model="name" placeholder="氏名" />
        <p v-if="!isValidName && isNameTyped" class="error">
          有効な氏名を入力してください
        </p>
      </div>
  
      <!-- email -->
      <div class="m-1">
        <input type="text" v-model="email" placeholder="email" />
      </div>
  
      <p class="m-1">
        新しいパスワードを入力してください。
        （大文字小文字を含む8文字以上24文字以内で入力してください）
      </p>
      <!-- 新しいパスワード -->
      <div class="m-1">
        <input type="password" v-model="password" placeholder="パスワード" />
        <p v-if="!isValidPasswd && isPasswdTyped" class="error">
          有効なパスワードを入力してください
        </p>
      </div>
  
      <!-- 新しいパスワード（確認） -->
      <div class="m-1">
        <input
          type="password"
          v-model="confirmation"
          placeholder="パスワード（確認）"
        />
        <p v-if="!isValidPWConfirm && isPWConfirmTyped" class="error">
          パスワードが一致しません
        </p>
      </div>
  
      <!-- ボタン -->
      <div class="m-3">
        <button
          class="btn btn-primary"
          @click="signup"
        >
          登録
        </button>
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
        name: "",
        };
    },
    setup(){
        
    },
    mounted() {
        

    },
    methods: {
        signup: async function(){
            let url = process.env.VUE_APP_API_DEV + '/provisional_signup';
            const response = await axios.post(url, {email: this.email, name: this.name, hashed_password: this.password});
            console.log("response.data = ", response.data)
            router.push('/login')
        },
        
    },
}
</script>