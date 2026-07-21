const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the start of mobile version
const mobileStartMarker = '<!-- ========== Mobile Version (Hidden on Desktop) ========== -->';
const startIndex = html.indexOf(mobileStartMarker);

if (startIndex > 0) {
  // Keep everything before the mobile section
  const beforeMobile = html.substring(0, startIndex);
  
  // Create new clean mobile HTML (using emoji icons instead of SVG to avoid parsing issues)
  const newMobileHTML = `
<!-- ========== Mobile Version (Hidden on Desktop) ========== -->
<div class="mobile-only mobile-container">

  <!-- Status Bar -->
  <div class="mobile-status-bar">
    <span class="status-time" id="mobileTime">17:00</span>
    <div class="status-icons">
      <span>📶</span><span>📡</span><span>🔋</span>
    </div>
  </div>

  <!-- Header -->
  <div class="mobile-header">
    <span class="mobile-logo">luobox</span>
    <button class="mobile-search-btn" onclick="document.getElementById('mobileSearchInput').focus()">🔍</button>
  </div>

  <!-- Hero Banner -->
  <div class="mobile-hero">
    <h1 class="mobile-hero-title">发现精彩网站</h1>
    <p class="mobile-hero-subtitle">10 大分类 · 500+ 精选网站</p>
    <div class="mobile-search-box">
      <span>🔍</span>
      <input type="text" placeholder="搜索网站..." id="mobileSearchInput" />
    </div>
  </div>

  <!-- Content Area -->
  <div class="mobile-content">

    <!-- Video Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #EF4444;">▶</div>
          <h2 class="mobile-cat-title">视频网站</h2>
        </div>
        <a href="video.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.bilibili.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FB7185;">B</div><span class="mobile-card-name">哔哩哔哩</span></div>
          <p class="mobile-card-desc">国内最大弹幕视频平台</p>
        </a>
        <a href="https://www.youtube.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FF0000;">▶</div><span class="mobile-card-name">YouTube</span></div>
          <p class="mobile-card-desc">全球最大视频分享平台</p>
        </a>
        <a href="https://www.iqiyi.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #00BE06;">爱</div><span class="mobile-card-name">爱奇艺</span></div>
          <p class="mobile-card-desc">海量正版高清视频</p>
        </a>
        <a href="https://v.qq.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FF6600;">腾</div><span class="mobile-card-name">腾讯视频</span></div>
          <p class="mobile-card-desc">热门综艺电视剧首播</p>
        </a>
        <a href="https://www.douyin.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #000000;">抖</div><span class="mobile-card-name">抖音</span></div>
          <p class="mobile-card-desc">记录美好生活短视频</p>
        </a>
        <a href="video.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Knowledge Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #3B82F6;">📚</div>
          <h2 class="mobile-cat-title">知识网站</h2>
        </div>
        <a href="knowledge.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.zhihu.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #0084FF;">知</div><span class="mobile-card-name">知乎</span></div>
          <p class="mobile-card-desc">专业问答知识社区</p>
        </a>
        <a href="https://www.baidu.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #2932E1;">百</div><span class="mobile-card-name">百度</span></div>
          <p class="mobile-card-desc">全球最大中文搜索引擎</p>
        </a>
        <a href="knowledge.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Literature Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #F59E0B;">📖</div>
          <h2 class="mobile-cat-title">文学网站</h2>
        </div>
        <a href="literature.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.qidian.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #ED424B;">起</div><span class="mobile-card-name">起点中文网</span></div>
          <p class="mobile-card-desc">正版原创文学阅读平台</p>
        </a>
        <a href="https://www.jjwxc.net" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #E91E63;">晋</div><span class="mobile-card-name">晋江文学城</span></div>
          <p class="mobile-card-desc">女性向原创文学网站</p>
        </a>
        <a href="literature.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- News Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #EF4444;">📰</div>
          <h2 class="mobile-cat-title">资讯网站</h2>
        </div>
        <a href="news.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.36kr.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #3399FF;">36</div><span class="mobile-card-name">36氪</span></div>
          <p class="mobile-card-desc">科技创业新闻资讯</p>
        </a>
        <a href="https://www.sina.com.cn" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FF6600;">新</div><span class="mobile-card-name">新浪网</span></div>
          <p class="mobile-card-desc">门户网站综合服务</p>
        </a>
        <a href="news.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Shop Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #8B5CF6;">🛒</div>
          <h2 class="mobile-cat-title">电商网站</h2>
        </div>
        <a href="shop.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.taobao.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FF5000;">淘</div><span class="mobile-card-name">淘宝</span></div>
          <p class="mobile-card-desc">万能购物平台</p>
        </a>
        <a href="https://www.jd.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #E4393C;">京</div><span class="mobile-card-name">京东</span></div>
          <p class="mobile-card-desc">品质购物首选</p>
        </a>
        <a href="shop.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Game Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #10B981;">🎮</div>
          <h2 class="mobile-cat-title">游戏网站</h2>
        </div>
        <a href="game.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.steamgames.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #1A9FFF;">S</div><span class="mobile-card-name">Steam</span></div>
          <p class="mobile-card-desc">全球游戏平台</p>
        </a>
        <a href="https://www.4399.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FF6600;">4399</div><span class="mobile-card-name">4399游戏</span></div>
          <p class="mobile-card-desc">在线小游戏平台</p>
        </a>
        <a href="game.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Tool & Design Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #06B6D4;">🛠️</div>
          <h2 class="mobile-cat-title">工具与设计</h2>
        </div>
        <a href="tool.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.canva.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #7C3AED;">C</div><span class="mobile-card-name">Canva可画</span></div>
          <p class="mobile-card-desc">在线设计工具</p>
        </a>
        <a href="https://github.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #181717;">Git</div><span class="mobile-card-name">GitHub</span></div>
          <p class="mobile-card-desc">代码托管平台</p>
        </a>
        <a href="tool.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Music Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #EC4899;">🎵</div>
          <h2 class="mobile-cat-title">音乐网站</h2>
        </div>
        <a href="music.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://y.qq.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #31C27C;">QQ</div><span class="mobile-card-name">QQ音乐</span></div>
          <p class="mobile-card-desc">海量音乐在线听</p>
        </a>
        <a href="https://music.163.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #C20C0C;">云</div><span class="mobile-card-name">网易云音乐</span></div>
          <p class="mobile-card-desc">发现好音乐</p>
        </a>
        <a href="music.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Finance Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #F59E0B;">💰</div>
          <h2 class="mobile-cat-title">金融理财</h2>
        </div>
        <a href="finance.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://xueqiu.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #F5A623;">雪</div><span class="mobile-card-name">雪球</span></div>
          <p class="mobile-card-desc">股票基金投资社区</p>
        </a>
        <a href="https://www.eastmoney.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #E60012;">东</div><span class="mobile-card-name">东方财富</span></div>
          <p class="mobile-card-desc">专业财经数据平台</p>
        </a>
        <a href="finance.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

    <!-- Life Services Category -->
    <section class="mobile-category-section">
      <div class="mobile-cat-header">
        <div class="mobile-cat-left">
          <div class="mobile-cat-icon" style="background: #10B981;">🏠</div>
          <h2 class="mobile-cat-title">生活服务</h2>
        </div>
        <a href="life.html" class="mobile-more-link">更多 ›</a>
      </div>
      <div class="mobile-card-grid">
        <a href="https://www.meituan.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #FFD100;">美团</div><span class="mobile-card-name">美团</span></div>
          <p class="mobile-card-desc">吃喝玩乐一站搞定</p>
        </a>
        <a href="https://www.ctrip.com" target="_blank" class="mobile-site-card">
          <div class="mobile-card-top"><div class="mobile-card-icon-bg" style="background: #2F9BFD;">携</div><span class="mobile-card-name">携程旅行</span></div>
          <p class="mobile-card-desc">酒店机票火车票预订</p>
        </a>
        <a href="life.html" class="mobile-more-card"><span class="mobile-more-plus">+</span><span class="mobile-more-text">更多</span></a>
      </div>
    </section>

  </div><!-- End .mobile-content -->

  <!-- Bottom Tab Bar -->
  <nav class="mobile-bottom-bar">
    <div class="mobile-pill">
      <a href="#" class="mobile-tab active"><span>🏠</span><span class="tab-label">首页</span></a>
      <a href="#" class="mobile-tab"><span>🧭</span><span class="tab-label">发现</span></a>
      <a href="#" class="mobile-tab"><span>👤</span><span class="tab-label">我的</span></a>
    </div>
  </nav>

</div><!-- End .mobile-container -->

<script>
function updateMobileTime() {
  var now = new Date();
  var h = String(now.getHours()).padStart(2,'0');
  var m = String(now.getMinutes()).padStart(2,'0');
  var el = document.getElementById('mobileTime');
  if(el) el.textContent = h+':'+m;
}
updateMobileTime(); setInterval(updateMobileTime,60000);
var si=document.getElementById('mobileSearchInput');
if(si){si.addEventListener('keydown',function(e){if(e.key==='Enter'&&this.value.trim()){window.location.href='https://www.baidu.com/s?wd='+encodeURIComponent(this.value.trim());}});}
document.querySelectorAll('.mobile-tab').forEach(function(t){t.addEventListener('click',function(e){e.preventDefault();document.querySelectorAll('.mobile-tab').forEach(function(x){x.classList.remove('active');});this.classList.add('active');});});
</script>

</body>
</html>`;

  // Write the complete file
  const finalHTML = beforeMobile + newMobileHTML;
  fs.writeFileSync('index.html', finalHTML, 'utf8');
  
  console.log('✅ Mobile section replaced successfully!');
  console.log('New file size:', (finalHTML.length / 1024).toFixed(1), 'KB');
} else {
  console.log('❌ Could not find mobile section marker');
}
