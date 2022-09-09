<template>
    <article>
<div class="side">
    <p>サイドバー</p>
</div>

<div class="content">
    <p>メインコンテンツ</p>
</div>
</article>

</template>

<style scoped>
    body{
        font-family:'Noto Sans JP',sans-serif;
        background-color:#f6f5f4;
    }
    .side{
        background-color:#ff838b;
        width:100px;
        height:300px;
        text-align:center;
    }

    .coontent{
        background-color:#b3d874;
        width:250px;
        height:300px;
        text-align:center;
        margin-left:10px;
    }

    article{
        display:flex;
    }
</style>