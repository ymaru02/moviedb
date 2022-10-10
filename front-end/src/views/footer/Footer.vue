<template>
  <div class="footer_box ">
    <div class="box_layout ">
      <div class="box_font">
        <!-- 아이콘 -->
      </div>
      <div class="info_layout">
        <ul class="info_pst">
          <p>자막 및 음성</p>
          <p>미디어 센터</p>
          <p>개인정보</p>
          <p>문의하기</p>
        </ul>
        <ul>
          <p>음성지원</p>
          <p>투자 정보</p>
          <p>법적 고지</p>
        </ul>
        <ul>
          <p>고객 센터</p>
          <p>입사 정보</p>
          <p>쿠키설정</p>
        </ul>
      </div>
      <ul class="company_info_layout company_info">
        <p>
          Movie DB
        </p>
        <p>대표: Movie DB</p>

        <p>
          주소 : 대전광역시 유성구 지족동로
        </p>
        <p>사업자 등록번호 : 12345-12331-12314</p>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.footer_box {
  /* display: flex;
    justify-content: center;
    padding: 5px;
    background-color: #000000;
    color: #fff; */
  background-color: black;
  margin-top: -20px;
}

.box_layout {
  display: flex;
  flex-direction: column;
  max-width: 980px;
  margin: 20px auto 0;
  padding: 0 4%;
  color: rgb(255, 255, 255);
}

.box_font {
  display: flex;
  margin-bottom: 1em;
}

.box_icon {
  height: 25px;
  width: 36px;
  color: gray;
}

.box_iconsize {
  font-size: 30px;
}

.info_layout {
  display: flex;
  justify-content: space-between;
  margin: 0 0 14px 0;
  font-size: 13px;
}

.info_pst {
  line-height: 3;
}

.company_info_layout {
  display: flex;
  flex-direction: column;
}

.company_info {
  font-size: 11px;
  line-height: 2;
}
</style>
