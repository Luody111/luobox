#!/usr/bin/env python3
"""Generate 10 secondary category pages for luobox navigation site."""
import os

OUTPUT_DIR = r"C:\Users\DELL\WorkBuddy\2026-07-21-17-00-36\surf-nav"

# ============================================================
# SITE DATA: 10 categories, each 50+ sites
# Format: (name, url, description, brand_color)
# ============================================================

VIDEO_SITES = [
    # Main page top 5
    ("抖音", "https://www.douyin.com", "记录美好生活", "#FE2C55"),
    ("哔哩哔哩", "https://www.bilibili.com", "国内知名视频弹幕网站", "#00A1D6"),
    ("YouTube", "https://www.youtube.com", "全球最大视频平台", "#FF0000"),
    ("快手", "https://www.kuaishou.com", "拥抱每一种生活", "#FF6B00"),
    ("优酷", "https://www.youku.com", "这世界很酷", "#00A1D6"),
    # Additional 45+
    ("西瓜视频", "https://www.ixigua.com", "给你新鲜好看", "#FF9000"),
    ("芒果TV", "https://www.mgtv.com", "青春湖南 芒果出品", "#FF5C00"),
    ("爱奇艺", "https://www.iqiyi.com", "爱奇艺·悦享品质", "#00BE06"),
    ("腾讯视频", "https://v.qq.com", "不负好时光", "#FF0000"),
    ("搜狐视频", "https://tv.sohu.com", "搜狐视频 综合平台", "#EA1E0C"),
    ("PP视频", "https://www.pptv.com", "聚精彩 偶遇你", "#FF6600"),
    ("乐视视频", "https://www.le.com", "乐视视频 生态体验", "#EE1C25"),
    ("咪咕视频", "https://www.miguvideo.com", "中国移动 视频平台", "#F5A623"),
    ("央视频", "https://yangshipin.cn", "中央广播电视总台", "#E60012"),
    ("抖音火山版", "https://www.hoshan.net", "火山小视频", "#FE2C55"),
    ("微视", "https://weishi.qq.com", "腾讯旗下短视频", "#1E88E5"),
    ("好看视频", "https://haokan.baidu.com", "百度短视频平台", "#06A7FF"),
    ("小红书视频", "https://www.xiaohongshu.com", "标记我的生活", "#FE2C55"),
    ("AcFun", "https://www.acfun.cn", "认真你就输啦", "#FDAC33"),
    ("网易CC直播", "https://cc.163.com", "网易游戏直播", "#E31436"),
    ("斗鱼直播", "https://www.douyu.com", "每个人的直播平台", "#FF6A00"),
    ("虎牙直播", "https://www.huya.com", "虎牙直播 不止于直播", "#EB7B55"),
    ("YY直播", "https://www.yy.com", "全民娱乐直播", "#FF5000"),
    ("抖音直播", "https://live.douyin.com", "抖音直播 热门不断", "#FE2C55"),
    ("快手直播", "https://live.kuaishou.com", "快手直播 真实记录", "#FF4900"),
    ("B站直播", "https://live.bilibili.com", "哔哩哔哩直播", "#FB7299"),
    ("Netflix", "https://www.netflix.com", "全球流媒体巨头", "#E50914"),
    ("Disney+", "https://www.disneyplus.com", "迪士尼流媒体", "#113CCF"),
    ("HBO Max", "https://www.hbomax.com", "华纳兄弟流媒体", "#B024AB"),
    ("Amazon Prime Video", "https://www.primevideo.com", "亚马逊会员视频", "#00A8E1"),
    ("Apple TV+", "https://tv.apple.com", "苹果原创内容", "#1D1D1F"),
    ("Hulu", "https://www.hulu.com", "美国流媒体平台", "#1CE783"),
    ("Vimeo", "https://vimeo.com", "专业视频分享社区", "#1AB7EA"),
    ("Dailymotion", "https://www.dailymotion.com", "国际视频分享平台", "#00D6F9"),
    ("Twitch", "https://www.twitch.tv", "全球游戏直播平台", "#9146FF"),
    ("Niconico", "https://www.nicovideo.jp", "日本弹幕视频网站", "#27282D"),
    ("抖音开放平台", "https://open.douyin.com", "抖音开发者平台", "#25F4EE"),
    ("西瓜创作平台", "https://creator.ixigua.com", "西瓜视频创作者中心", "#FF9000"),
    ("B站创作中心", "https://member.bilibili.com", "B站UP主后台", "#FB7299"),
    ("YouTube Studio", "https://studio.youtube.com", "YouTube 创作者工作室", "#FF0000"),
    ("快手创作者中心", "https://cp.kuaishou.com", "快手创作者平台", "#FF4900"),
    ("微博视频", "https://weibo.com/tv", "微博视频 随时随地", "#FF8200"),
    ("微信视频号", "https://channels.weixin.qq.com", "微信短视频平台", "#07C160"),
    ("知乎视频", "https://www.zhihu.com/video", "知乎 视频频道", "#0084FF"),
    ("豆瓣时间", "https://time.douban.com", "豆瓣知识付费", "#007722"),
    ("得到App", "https://www.dedao.cn", "知识就在得到", "#002C3E"),
    ("蜻蜓FM", "https://www.qingting.fm", "有声内容聚合平台", "#29B6F3"),
    ("喜马拉雅", "https://www.ximalaya.com", "中国领先音频平台", "#ED5858"),
    ("网易云音乐", "https://music.163.com", "发现好音乐", "#C20C0C"),
    ("QQ音乐", "https://y.qq.com", "海量正版音乐在线听", "#31C27C"),
    ("酷狗音乐", "https://www.kugou.com", "就是歌多", "#0DC070"),
]

KNOWLEDGE_SITES = [
    ("知网", "https://www.cnki.net", "中国学术文献网络总库", "#1A5490"),
    ("维基百科", "https://zh.wikipedia.org", "自由的百科全书", "#666666"),
    ("百度百科", "https://baike.baidu.com", "中文互联网知识平台", "#2962FF"),
    ("懂客", "https://www.dongde.cn", "多领域知识短视频", "#FF6B00"),
    ("万方数据", "https://www.wanfangdata.com.cn", "中外学术数据平台", "#00A1D6"),
    ("ResearchGate", "https://www.researchgate.net", "全球学者社交网络", "#00C853"),
    ("谷歌学术", "https://scholar.google.com", "免费学术搜索引擎", "#4285F4"),
    ("百度学术", "https://xueshu.baidu.com", "中文学术搜索引擎", "#2932E1"),
    ("知乎", "https://www.zhihu.com", "有问题上知乎", "#0084FF"),
    ("豆瓣", "https://www.douban.com", "书影音兴趣小组", "#007722"),
    ("Quora", "https://www.quora.com", "英文问答社区", "#B92B27"),
    ("Stack Overflow", "https://stackoverflow.com", "程序员问答社区", "#F48024"),
    ("MDN Web Docs", "https://developer.mozilla.org", "Web开发权威文档", "#000000"),
    ("W3Schools", "https://www.w3schools.com", "在线编程教程", "#04AA6D"),
    ("Runoob", "https://www.runoob.com", "菜鸟编程教程", "#4CAF50"),
    ("慕课网", "https://www.imooc.com", "IT技能学习平台", "#FF5722"),
    ("网易云课堂", "https://study.163.com", "实用技能学习平台", "#FF4400"),
    ("腾讯课堂", "https://ke.qq.com", "专业在线教育平台", "#12B7F5"),
    ("学堂在线", "https://www.xuetangx.com", "清华大学MOOC平台", "#CF0A2C"),
    ("中国大学MOOC", "https://www.icourse163.org", "教育部合作MOOC", "#2073C9"),
    ("Coursera", "https://www.coursera.org", "全球顶尖大学课程", "#0056D2"),
    ("edX", "https://www.edx.org", "哈佛MIT在线课程", "#02262B"),
    ("Udemy", "https://www.udemy.com", "全球最大在线课程平台", "#A435F0"),
    ("Khan Academy", "https://www.khanacademy.org", "可汗学院 免费教育", "#14BF96"),
    ("TED演讲", "https://www.ted.com", "值得传播的思想", "#E62B1E"),
    ("网易公开课", "https://open.163.com", "名校公开课合集", "#2AACE5"),
    ("超星学习通", "https://i.chaoxing.com", "移动学习综合平台", "#1890FF"),
    ("智慧树", "https://www.zhihuishu.com", "高校学分课平台", "#52C41A"),
    ("学而思网校", "https://www.xueersi.com", "K12在线教育", "#FF6600"),
    ("猿辅导", "https://www.yuanfudao.com", "中小学在线辅导", "#FF6B00"),
    ("作业帮", "https://www.zybang.com", "拍照搜题工具", "#5B8FF9"),
    ("粉笔", "https://www.fenbi.com", "公考职业培训", "#FF6B35"),
    ("中公网校", "https://e.offcn.com", "公职考试培训", "#E03E26"),
    ("华图在线", "https://v.huatu.com", "公务员考试备考", "#E74C3C"),
    ("IT之家", "https://www.ithome.com", "科技资讯与教程", "#1E90FF"),
    ("InfoQ中文站", "https://www.infoq.cn", "技术驱动创新", "#D92D2D"),
    ("掘金", "https://juejin.cn", "技术社区与博客", "#1E80FF"),
    ("CSDN", "https://www.csdn.net", "开发者技术社区", "#F26522"),
    ("博客园", "https://www.cnblogs.com", "开发者博客社区", "#1A8CD1"),
    ("SegmentFault", "https://segmentfault.com", "中文技术问答", "#009E96"),
    ("开源中国", "https://www.oschina.net", "开源技术资讯社区", "#3498DB"),
    ("V2EX", "https://www.v2ex.com", "创意工作者的社区", "#333333"),
    ("少数派", "https://sspai.com", "数字生活指南", "#DA282A"),
    ("果壳", "https://www.guokr.com", "科技主题科普社区", "#43CE17"),
    ("丁香园", "https://www.dxy.com", "医疗领域专业社区", "#3CB371"),
    ("医学微视", "https://www.mvyxws.com", "医学科普视频平台", "#19BE6B"),
    ("喜马拉雅", "https://www.ximalaya.com", "中国领先音频平台", "#ED5858"),
    ("MBA智库", "https://wiki.mbalib.com", "经管百科知识库", "#1E87F0"),
    ("经管之家", "https://bbs.pinggu.org", "经济管理论坛", "#E65100"),
    ("IT桔子", "https://www.itjuzi.com", "创业投资数据库", "#FF6B00"),
    ("企查查", "https://www.qcc.com", "企业信息查询平台", "#2962FF"),
    ("天眼查", "https://www.tianyancha.com", "商业查询平台", "#2F54EB"),

]

LITERATURE_SITES = [
    ("起点中文网", "https://www.qidian.com", "阅文集团旗下原创平台", "#BF360C"),
    ("晋江文学城", "https://www.jjwxc.net", "女性向小说阅读平台", "#E53935"),
    ("潇湘书院", "https://www.xxsy.net", "女生原创电子阅读", "#E91E63"),
    ("豆瓣读书", "https://book.douban.com", "读书人的精神角落", "#43A047"),
    ("纵横中文网", "http://www.zongheng.com", "畅享创作乐趣", "#F9A825"),
    ("七猫小说", "https://www.qimao.com", "免费看小说追书神器", "#7B1FA2"),
    ("番茄小说", "https://fanqie.novel.com", "免费小说阅读APP", "#F44336"),
    ("飞卢小说网", "https://b.faloo.com", "网络小说原创平台", "#E64A19"),
    ("小说阅读网", "https://www.readnovel.com", "热门小说免费读", "#FF7043"),
    ("纵横女生网", "http://girls.zongheng.com", "女生原创文学", "#EC407A"),
    ("红袖添香", "https://www.hongxiu.com", "女性原创小说网", "#E91E63"),
    ("言情小说吧", "https://www.yqxs.com", "言情小说阅读基地", "#F48FB1"),
    ("起点女生网", "https://nvl.qidian.com", "起点女频频道", "#EF5350"),
    ("云起书院", "https://yunqi.qq.com", "腾讯云起女频平台", "#FF6B6B"),
    ("若初文学网", "https://www.ruochuwang.com", "原创网络文学", "#BA68C8"),
    ("磨铁阅读", "https://read.motie.com", "磨铁旗下阅读平台", "#EF6C00"),
    ("连尚文学", "https://www.lianshangwenxue.com", "免费阅读平台", "#FF5722"),
    ("掌阅", "https://www.ireader.com", "数字阅读领导品牌", "#1565C0"),
    ("QQ阅读", "https://book.qq.com", "QQ阅读 海量正版", "#12B7F5"),
    ("微信读书", "https://weread.qq.com", "微信读书 正版电子书", "#07C160"),
    ("豆瓣读书", "https://book.douban.com", "书影音全记录", "#007722"),
    ("当当读书", "https://book.dangdang.com", "当当网电子书店", "#E4393C"),
    ("亚马逊Kindle", "https://www.amazon.cn/kindle", "全球电子阅读器", "#FF9900"),
    ("京东读书", "https://e-book.jd.com", "京东电子书平台", "#E4393C"),
    ("网易云阅读", "https://yuedu.163.com", "网易精品阅读", "#1E90FF"),
    ("阿里文学", "https://www.aliwx.com", "阿里旗下阅读平台", "#FF6A00"),
    ("百度文库", "https://wenku.baidu.com", "在线文档分享平台", "#2932E1"),
    ("豆丁文档", "https://www.docin.com", "中文文档分享平台", "#FF6600"),
    ("道客巴巴", "https://www.doc88.com", "在线文档共享", "#FF8C00"),
    ("原创力文档", "https://www.book118.com", "文档上传下载", "#4CAF50"),
    ("360个人图书馆", "http://www.360doc.com", "个人图书馆收藏夹", "#FF4500"),
    ("国学网", "http://www.guoxue.com", "中华传统文化门户", "#8B4513"),
    ("古诗文网", "https://so.gushiwen.cn", "古诗文检索鉴赏", "#795548"),
    ("诗词名句网", "https://www.shicimingju.com", "经典诗词名句大全", "#5D4037"),
    ("全本小说网", "https://www.qb5200.co", "全本小说免费阅读", "#FF7043"),
    ("顶点小说", "https://www.23us.cc", "免费小说更新快", "#E64A19"),
    ("笔趣阁", "https://www.biquge5200.com", "小说更新最快", "#F44336"),
    ("笔趣看", "https://www.biqukan.com", "免费小说阅读网", "#E91E63"),
    ("八一中文网", "https://81new.com", "军事历史小说", "#1565C0"),
    ("玄幻小说网", "https://www.xuanhuan.com", "玄幻奇幻作品集", "#673AB7"),
    ("悬疑推理网", "https://www.xuanyi.org", "悬疑推理作品", "#37474F"),
    ("散文网", "https://www.sanweng.com", "散文随笔精选", "#8D6E63"),
    ("诗歌库", "https://www.shigeku.com", "现代诗歌作品库", "#5C6BC0"),
    ("儿童文学网", "https://www.61wen.com", "少儿读物平台", "#FFCA28"),
    ("科幻小说网", "https://www.khxxw.com", "科幻作品专区", "#00BCD4"),
    ("晋江文学城手机版", "https://m.jjwxc.net", "JJWXC移动端阅读", "#E53935"),
    ("起点国际版", "https://www.webnovel.com", "起点海外网文平台", "#BF360C"),
    ("纵横中文网", "http://www.zongheng.com", "男生原创小说平台", "#F9A825"),
    ("逐浪小说网", "https://www.zhulang.com", "原创网络文学基地", "#E65100"),
    ("红薯中文网", "https://www.hongshu.com", "言情小说创作阅读", "#EC407A"),
]

NEWS_SITES = [
    ("今日头条", "https://www.toutiao.com", "信息创造价值", "#D32F2F"),
    ("36氪", "https://36kr.com", "科技创业媒体平台", "#2196F3"),
    ("新浪新闻", "https://news.sina.com.cn", "门户网站综合服务", "#E53935"),
    ("网易新闻", "https://news.163.com", "各有态度的门户", "#C62828"),
    ("搜狐新闻", "https://news.sohu.com", "门户新闻客户端", "#E53935"),
    ("腾讯新闻", "https://news.qq.com", "即时全球资讯尽览", "#1E88E5"),
    ("新华网", "http://www.xinhuanet.com", "新华社官方网站", "#D32F2F"),
    ("人民网", "http://www.people.com.cn", "人民日报官方网站", "#C62828"),
    ("央视新闻", "http://news.cctv.com", "中央电视台新闻", "#E53935"),
    ("光明网", "http://www.gmw.cn", "光明日报官方网站", "#D32F2F"),
    ("中国新闻网", "http://www.chinanews.com", "中国新闻社官网", "#C62828"),
    ("环球时报", "https://globaltimes.cn", "解读中国 解读世界", "#E53935"),
    ("澎湃新闻", "https://www.thepaper.cn", "专注时政思想", "#D32F2F"),
    ("界面新闻", "https://www.jiemian.com", "只服务于独立思考者", "#1565C0"),
    ("财新网", "https://www.caixin.com", "财经新闻专业媒体", "#0D47A1"),
    ("第一财经", "https://www.yicai.com", "专业财经媒体", "#E65100"),
    ("华尔街见闻", "https://wallstreetcn.com", "全球财经即时通讯", "#212121"),
    ("虎嗅网", "https://www.huxiu.com", "聚合优质创新信息", "#F44336"),
    ("钛媒体", "https://www.tmtpost.com", "科技商业新媒体", "#1E88E5"),
    ("雷锋网", "https://www.leiphone.com", "科技媒体与服务平台", "#212121"),
    ("极客公园", "https://www.geekpark.net", "科技创新者社区", "#1A73E8"),
    ("爱范儿", "https://www.ifanr.com", "未来生活方式媒体", "#00B51D"),
    ("少数派", "https://sspai.com", "数字生活指南", "#DA282A"),
    ("IT之家", "https://www.ithome.com", "科技资讯门户", "#1E90FF"),
    ("驱动中国", "https://www.qudong.com", "科技产业媒体", "#E53935"),
    ("中关村在线", "https://www.zol.com.cn", "科技产品门户", "#FF6600"),
    ("太平洋电脑网", "https://pc.pconline.com.cn", "IT产品导购平台", "#0066B3"),
    ("凤凰网", "https://news.ifeng.com", "凤凰网新闻频道", "#E53935"),
    ("环球网", "http://www.huanqiu.com", "环球时报新媒体", "#D32F2F"),
    ("观察者网", "https://www.guancha.cn", "中国关怀 全球视野", "#B71C1C"),
    ("联合早报", "https://www.zaobao.com.sg", "新加坡华文日报", "#D32F2F"),
    ("BBC中文", "https://www.bbc.com/zhongwen/simp", "BBC中文频道", "#BB1919"),
    ("CNN中文", "https://edition.cnn.com/cnn10", "CNN十点新闻摘要", "#CC0000"),
    ("路透社", "https://cn.reuters.com", "路透社中文网", "#FF8000"),
    ("金融界", "https://www.jrj.com.cn", "财经证券资讯", "#E53935"),
    ("东方财富", "https://www.eastmoney.com", "财经股票门户", "#E53935"),
    ("同花顺", "https://www.10jqka.com.cn", "投资理财平台", "#E53935"),
    ("雪球", "https://xueqiu.com", "投资者交流社区", "#1E88E5"),
    ("格隆汇", "https://www.gelonghui.com", "海外投资研究平台", "#1E88E5"),
    ("汽车之家", "https://www.autohome.com.cn", "汽车资讯门户", "#E53935"),
    ("易车网", "https://www.yiche.com", "汽车报价导购平台", "#1565C0"),
    ("懂车帝", "https://www.dongchedi.com", "汽车资讯APP", "#1E88E5"),
    ("体育头条", "https://www.tiyutoutiao.com", "体育新闻聚合", "#F44336"),
    ("虎扑体育", "https://bbs.hupu.com", "体育迷论坛", "#E65100"),
    ("直播吧", "https://www.zhibo8.com", "体育赛事直播", "#E53935"),
    ("澎湃新闻", "https://www.thepaper.cn", "专注时政思想", "#D32F2F"),
    ("界面新闻", "https://www.jiemian.com", "只服务于独立思考者", "#1565C0"),
    ("财新网", "https://www.caixin.com", "财经新闻专业媒体", "#0D47A1"),
    ("第一财经", "https://www.yicai.com", "专业财经媒体", "#E65100"),
    ("华尔街见闻", "https://wallstreetcn.com", "全球财经即时通讯", "#212121"),

]

SHOP_SITES = [
    ("淘宝", "https://www.taobao.com", "万能购物平台", "#FF5000"),
    ("京东", "https://www.jd.com", "多快好省购物体验", "#E4393C"),
    ("拼多多", "https://www.pinduoduo.com", "拼着买更便宜", "#FF6A00"),
    ("小红书", "https://www.xiaohongshu.com", "标记我的生活", "#F27524"),
    ("唯品会", "https://www.vip.com", "品牌特卖平台", "#E02E24"),
    ("天猫", "https://www.tmall.com", "品牌旗舰正品", "#FF2741"),
    ("苏宁易购", "https://www.suning.com", "苏宁易购 专注服务", "#F60"),
    ("国美在线", "https://www.gome.com.cn", "国美电器网上商城", "#E60012"),
    ("1号店", "https://www.yhd.com", "网上超市 一小时达", "#E43130"),
    ("当当网", "https://www.dangdang.com", "网上购物 当当最好", "#E4393C"),
    ("亚马逊中国", "https://www.amazon.cn", "亚马逊 中国站点", "#FF9900"),
    ("考拉海购", "https://www.kaola.com", "跨境进口电商平台", "#FF6600"),
    ("洋码头", "https://www.yangmatou.com", "海外直邮购物平台", "#E65100"),
    ("寺库", "https://www.secoo.com", "奢侈品电商", "#000000"),
    ("得物", "https://www.dewu.com", "球鞋潮牌鉴别交易", "#000000"),
    ("闲鱼", "https://www.goofish.com", "闲置二手交易平台", "#FF6A00"),
    ("转转", "https://www.zhuanzhuan.com", "二手交易平台", "#FF6B00"),
    ("微店", "https://www.weidian.com", "手机开店用微店", "#FF6600"),
    ("蘑菇街", "https://www.mogujie.com", "女性时尚消费平台", "#FF6600"),
    ("美丽说", "https://www.meilishuo.com", "女性时尚社区电商", "#FF6B6B"),
    ("聚划算", "https://ju.taobao.com", "淘宝特价团购", "#FF6A00"),
    ("美团优选", "https://www.meituan.com", "美团社区团购", "#FFC300"),
    ("盒马鲜生", "https://www.freshippo.com", "新零售生鲜超市", "#00A0E9"),
    ("每日优鲜", "https://www.meiguoyixian.com", "生鲜O2O平台", "#4CAF50"),
    ("叮咚买菜", "https://www.ddmall.com", "生鲜电商配送", "#00B365"),
    ("永辉超市", "https://www.yonghui.com.cn", "连锁零售超市", "#E53935"),
    ("大润发优鲜", "https://e.rt-mart.com.cn", "大润发线上商城", "#E53935"),
    ("山姆会员商店", "https://www.samsclub.cn", "高端会员制超市", "#E53935"),
    ("Costco开市客", "https://www.costco.com.cn", "会员制仓储超市", "#0064B8"),
    ("1688", "https://www.1688.com", "阿里巴巴批发采购", "#FF6A00"),
    ("阿里巴巴国际站", "https://www.alibaba.com", "B2B跨境电商平台", "#FF6A00"),
    ("敦煌网", "https://www.dhgate.com", "跨境电商B2B", "#FF6600"),
    ("速卖通", "https://www.aliexpress.com", "全球速卖通", "#FF6A00"),
    ("Wish", "https://www.wish.com", "移动端跨境电商平台", "#5A31F4"),
    ("Shopee", "https://shopee.com", "东南亚跨境电商", "#EE4D2D"),
    ("Lazada", "https://www.lazada.com.cn", "东南亚电商平台", "#0F146D"),
    ("有赞", "https://www.youzan.com", "商家SaaS服务平台", "#31B95B"),
    ("微盟", "https://www.weimob.com", "智慧商业服务商", "#1E88E5"),
    ("有赞零售", "https://retail.youzan.com", "新零售解决方案", "#31B95B"),
    ("拼多多商家版", "https://pms.pinduoduo.com", "拼多多商家后台", "#E02E24"),
    ("淘宝卖家中心", "https://sell.taobao.com", "淘宝卖家工作台", "#FF5000"),
    ("京东商家帮助", "https://help.jd.com/user/issue/list", "京东商家支持", "#E4393C"),
    ("抖音电商", "https://ecom.douyin.com", "抖音小店商家", "#161823"),
    ("快手电商", "https://seller.kuaishou.com", "快手商家后台", "#FF4900"),
    ("微信小商店", "https://shop.weixin.qq.com", "小程序电商工具", "#07C160"),
    ("什么值得买", "https://www.smzdm.com", "网购消费建议", "#E53935"),
    ("慢慢买", "https://www.manmanbuy.com", "全网比价查询", "#FF6600"),
    ("惠惠购物助手", "https://www.hhz.com", "购物比价浏览器插件", "#FF6600"),
    ("什么值得买Pro", "pro.smzdm.com", "消费决策平台专业版", "#E53935"),
    ("返利网", "https://www.fanli.com", "购物返利优惠", "#FF6B00"),
]

GAME_SITES = [
    ("Steam", "https://store.steampowered.com", "全球最大游戏发行平台", "#1B2838"),
    ("TapTap", "https://www.taptap.cn", "手游玩家首选社区", "#F4B942"),
    ("4399", "https://www.4399.com", "在线小游戏平台", "#FA9D3B"),
    ("游民星空", "https://www.gamersky.com", "游戏资讯与攻略", "#FFB74D"),
    ("Epic Games Store", "https://www.epicgames.com/store", "免费游戏大作领取", "#212121"),
    ("暴雪战网", "https://www.blizzard.com", "精品游戏聚合地", "#C62828"),
    ("Ubisoft Connect", "https://connect.ubisoft.com", "育碧游戏平台", "#0070FF"),
    ("EA App", "https://www.ea.com/ea-app-launcher", "EA游戏启动器", "#000000"),
    ("GOG Galaxy", "https://www.gog.com/galaxy", "DRM-free 游戏平台", "#863F00"),
    ("Itch.io", "https://itch.io", "独立游戏发布平台", "#FA5C5C"),
    ("GameSpot", "https://www.gamespot.com", "游戏评测与资讯", "#E53935"),
    ("IGN中国", "https://www.ign.com.cn", "全球游戏媒体中文站", "#E53935"),
    ("游侠网", "https://www.ali213.net", "单机游戏门户", "#FF6600"),
    ("3DMGAME", "https://www.3dmgame.com", "游戏资源下载", "#FF6600"),
    ("游迅网", "https://www.youxun.com", "游戏下载平台", "#FF9800"),
    ("九游", "https://www.9game.cn", "手游下载与攻略", "#FF6B00"),
    ("好游快爆", "https://www.qqugame.com", "手游推荐平台", "#FF6B35"),
    ("小黑盒", "https://www.xiaoheihe.cn", "游戏数据与社区", "#222222"),
    ("NGA玩家社区", "https://bbs.ngacn.cc", "电竞玩家聚集地", "#4CAF50"),
    ("电玩巴士", "https://www.tgbus.com", "主机游戏资讯", "#E53935"),
    ("机核网", "https://www.gcores.com", "硬核游戏文化社区", "#E65100"),
    ("篝火营地", "https://www.gamersky.com/handbook", "游戏文化媒体", "#FF6B00"),
    ("触乐", "https://www.chuapp.com", "优秀独立游戏媒体", "#1E88E5"),
    ("游戏葡萄", "https://www.youxiputao.com", "游戏产业媒体", "#9C27B0"),
    ("17173", "https://www.17173.com", "网络游戏第一门户", "#E53935"),
    ("太平洋游戏网", "https://pcgames.com.cn", "游戏综合门户", "#FF6600"),
    ("多玩游戏", "https://www.duowan.com", "游戏资讯社区", "#FF6600"),
    ("新浪游戏", "https://games.sina.com.cn", "新浪游戏频道", "#E53935"),
    ("腾讯游戏", "https://game.qq.com", "腾讯游戏官方平台", "#E53935"),
    ("网易游戏", "https://game.163.com", "网易游戏官网", "#E63C3C"),
    ("米哈游", "https://www.mihoyo.com", "米哈游游戏官网", "#1E88E5"),
    ("莉莉丝游戏", "https://www.lilith.com", "莉莉丝游戏官网", "#E91E63"),
    ("叠纸游戏", "https://www.infold.games", "叠纸游戏官网", "#EC407A"),
    ("鹰角网络", "https://arknights.global", "明日方舟开发商", "#1E88E5"),
    ("拳头游戏", "https://www.riotgames.com", "英雄联盟开发商", "#D1363A"),
    ("Valve", "https://www.valvesoftware.com", "Steam 开发商", "#171721"),
    ("Unity", "https://unity.com", "游戏引擎开发平台", "#000000"),
    ("Unreal Engine", "https://www.unrealengine.com", "虚幻引擎官方", "#313131"),
    ("Godot Engine", "https://godotengine.org", "开源游戏引擎", "#478CBF"),
    (" itch.io", "https://itch.io/game-assets", "游戏素材市场", "#FA5C5C"),
    ("Poly Pizza", "https://poly.pizza", "低多边形3D模型", "#FF6B6B"),
    ("Sketchfab", "https://sketchfab.com", "3D模型展示平台", "#16AFEF"),
    ("SteamDB", "https://steamdb.info", "Steam 数据统计", "#1B2838"),
    ("SteamSpy", "https://steamspy.com", "Steam 游戏数据分析", "#1B2838"),
    ("BoardGameGeek", "https://boardgamegeek.com", "桌游数据库", "#FF6600"),
    ("Mod DB", "https://www.moddb.com", "游戏模组下载", "#E65100"),
    ("Nexus Mods", "https://www.nexusmods.com", "游戏MOD社区", "#D97C2B"),
    ("Discord", "https://discord.com", "游戏玩家语音社区", "#5865F2"),
    ("Epic Games Launcher", "https://www.epicgames.com/store", "Epic游戏启动器", "#212121"),
    ("GOG Galaxy 2.0", "https://www.gog.com/galaxy", "全平台游戏库聚合", "#86300"),
    (" itch.io", "https://itch.io", "独立游戏平台", "#FA5C5C"),

]

TOOL_DESIGN_SITES = [
    # Tools - main page picks + more
    ("GitHub", "https://github.com", "全球代码托管平台", "#181717"),
    ("Notion", "https://www.notion.so", "全能笔记协作工具", "#222222"),
    ("ProcessOn", "https://www.processon.com", "免费在线流程图工具", "#4CAF50"),
    # Design tools merged in
    ("Canva 可画", "https://www.canva.com", "在线设计做图工具", "#00C4CC"),
    ("Figma", "https://www.figma.com", "协作式UI设计工具", "#A259FF"),
    ("站酷", "https://www.zcool.com.cn", "设计师互动平台", "#FDB300"),
    ("花瓣网", "https://huaban.com", "设计师灵感采集", "#FF5722"),
    ("千图网", "https://www.58pic.com", "免费设计素材下载", "#FF9800"),
    ("包图网", "https://ibaotu.com", "海量设计素材库", "#FF7043"),
    # More tools
    ("GitLab", "https://gitlab.com", "代码托管DevOps平台", "#FC6D26"),
    ("Gitee", "https://gitee.com", "国产代码托管平台", "#C71D23"),
    ("Bitbucket", "https://bitbucket.org", "Atlassian代码托管", "#2684FF"),
    ("Stack Overflow", "https://stackoverflow.com", "程序员问答社区", "#F48024"),
    ("VS Code", "https://code.visualstudio.com", "微软代码编辑器", "#007ACC"),
    ("Sublime Text", "https://www.sublimetext.com", "轻量级代码编辑器", "#FF9800"),
    ("JetBrains", "https://www.jetbrains.com", "专业IDE全家桶", "#000000"),
    ("CodePen", "https://codepen.io", "前端代码在线编辑", "#000000"),
    ("JSFiddle", "https://jsfiddle.net", "前端代码调试工具", "#4679A4"),
    ("Replit", "https://replit.com", "在线IDE编程环境", "#F26207"),
    ("CodeSandbox", "https://codesandbox.io", "在线代码沙箱环境", "#1E90FF"),
    ("Cloudflare Pages", "https://pages.cloudflare.com", "静态网站部署", "#F38020"),
    ("Vercel", "https://vercel.com", "前端部署平台", "#000000"),
    ("Netlify", "https://www.netlify.com", "自动化Web部署", "#00AD9F"),
    ("GitHub Pages", "https://pages.github.com", "GitHub静态托管", "#222222"),
    ("Docker Hub", "https://hub.docker.com", "容器镜像仓库", "#2496ED"),
    ("npm", "https://www.npmjs.com", "JavaScript包管理器", "#CB3837"),
    ("pnpm", "https://pnpm.io", "快速磁盘节省的包管理", "#F69220"),
    ("Yarn", "https://yarnpkg.com.js", "可靠依赖管理工具", "#2C8EBB"),
    ("Postman", "https://www.postman.com", "API开发测试工具", "#FF6C37"),
    ("Swagger", "https://swagger.io", "API文档生成工具", "#85EA2D"),
    ("Insomnia", "https://insomnia.rest", "API客户端调试工具", "#5C5CDE"),
    ("Figma Community", "https://community.figma.com", "Figma设计社区", "#A259FF"),
    ("Sketch", "https://www.sketch.com", "Mac原生UI设计工具", "#FDB300"),
    ("Adobe XD", "https://www.adobe.com/products/xd.html", "Adobe UI/UX设计工具", "#FF61F6"),
    ("Photoshop", "https://www.adobe.com/products/photoshop.html", "图像处理行业标准", "#31A8FF"),
    ("Illustrator", "https://www.adobe.com/products/illustrator.html", "矢量图形设计工具", "#FF9A00"),
    ("InDesign", "https://www.adobe.com/products/indesign.html", "专业排版设计软件", "#FF3366"),
    ("Premiere Pro", "https://www.adobe.com/products/premiere.html", "专业视频剪辑软件", "#9999FF"),
    ("After Effects", "https://www.adobe.com/products/aftereffects.html", "动态视觉特效软件", "#9999FF"),
    ("DaVinci Resolve", "https://www.blackmagicdesign.com/products/davinciresolve", "专业调色剪辑软件", "#1E88E5"),
    ("剪映", "https://www.capcut.cn", "字节跳动视频剪辑工具", "#00D6F9"),
    ("必剪", "https://www.bilibili.com/bcut", "B站出品的视频剪辑", "#FB7299"),
    (" OBS", "https://obsproject.com", "开源录屏直播软件", "#302E31"),
    ("Loom", "https://www.loom.com", "快速录制分享视频", "#625DF5"),
    ("Snipaste", "https://www.snipaste.com", "截图贴图神器", "#00ADEF"),
    ("ShareX", "https://getsharex.com", "开源截图录屏工具", "#1769AA"),
    ("TinyPNG", "https://tinypng.com", "智能图片压缩工具", "#009E77"),
    ("Squoosh", "https://squoosh.app", "Google图像压缩工具", "#4285F4"),
    ("remove.bg", "https://www.remove.bg", "AI一键抠图工具", "#2C66BC"),
    ("Photopea", "https://www.photopea.com", "在线免费PS替代", "#1ABC9C"),
    ("Excalidraw", "https://excalidraw.com", "手绘风格白板工具", "#6965DB"),
    ("Miro", "https://miro.com", "在线协作白板", "#FFD02F"),
    ("Trello", "https://trello.com", "看板式项目管理", "#0079BF"),
    ("Asana", "https://asana.com", "团队任务管理工具", "#F06A6A"),
    ("Monday.com", "https://monday.com", "团队协作操作系统", "#FF3D57"),
    ("Slack", "https://slack.com", "企业沟通协作平台", "#4A154B"),
    ("飞书", "https://www.feishu.cn", "字节企业协作平台", "#3370FF"),
    ("钉钉", "https://www.dingtalk.com", "阿里巴巴企业办公", "#0089FF"),
    ("企业微信", "https://work.weixin.qq.com", "微信企业版", "#1DAF72"),
    ("石墨文档", "https://shimo.im", "在线协同文档", "#20B968"),
    ("金山文档", "https://www.kdocs.cn", "WPS在线文档", "#2B579A"),
    ("语雀", "https://www.yuque.com", "蚂蚁集团知识库", "#1677FF"),
    ("飞书文档", "https://feishu.cn/docs", "飞书在线文档", "#3370FF"),
    ("腾讯文档", "https://docs.qq.com", "腾讯在线协作文档", "#0066FF"),
    ("Google Docs", "https://docs.google.com", "Google在线文档", "#4285F4"),
    ("Notion", "https://www.notion.so/zh-cn", "全能笔记与知识库", "#222222"),
    ("Obsidian", "https://obsidian.md", "本地知识库工具", "#7C3AED"),
    ("Logseq", "https://logseq.com", "开源双向链接笔记", "#5966FF"),
    ("Typora", "https://typoraio.io", "Markdown写作利器", "#1982C4"),
    ("XMind", "https://www.xmind.net", "思维导图软件", "#FF6B00"),
]

MUSIC_SITES = [
    # Main page top 5
    ("网易云音乐", "https://music.163.com", "发现好音乐", "#C20C0C"),
    ("QQ音乐", "https://y.qq.com", "海量正版音乐在线听", "#31C27C"),
    ("酷狗音乐", "https://www.kugou.com", "就是歌多", "#0DC070"),
    ("酷我音乐", "https://www.kuwo.cn", "好音质用酷我", "#D32F2F"),
    ("咪咕音乐", "https://music.migu.cn", "正版音乐畅听", "#F5A623"),
    # Additional 45+
    ("Apple Music", "https://music.apple.com", "苹果音乐流媒体", "#FA243C"),
    ("Spotify", "https://www.spotify.com", "全球最大流媒体平台", "#1DB954"),
    ("YouTube Music", "https://music.youtube.com", "谷歌旗下音乐平台", "#FF0000"),
    ("SoundCloud", "https://soundcloud.com", "全球音频社区", "#FF5500"),
    ("Bandcamp", "https://bandcamp.com", "独立音乐人平台", "#629AA9"),
    ("虾米音乐(停服)", "https://www.xiami.com", "阿里旗下音乐平台", "#FF6A00"),
    ("千千音乐", "http://music.taihe.com", "百度旗下音乐平台", "#3388FF"),
    ("5sing原创音乐", "https://5sing.kugou.com", "中国原创音乐基地", "#FF9800"),
    ("全民K歌", "https://kg.qq.com", "腾讯社交K歌应用", "#FFCC00"),
    ("唱吧", "https://changba.com", "手机K歌社交应用", "#FF3366"),
    ("酷狗唱唱", "https://changk.kugou.com", "酷狗K歌产品", "#0DC070"),
    ("网易云音乐人", "https://music.163.com/#/artist", "网易音乐人入驻平台", "#C20C0C"),
    ("QQ音乐开放平台", "https://y.qq.com/portal/music_open.html", "QQ音乐创作者服务", "#31C27C"),
    ("豆瓣FM", "https://douban.fm", "豆瓣个性化电台", "#007722"),
    ("落网", "https://luoo.net", "独立音乐播客电台", "#333333"),
    ("喜马拉雅FM", "https://www.ximalaya.com", "中文有声内容平台", "#ED5858"),
    ("蜻蜓FM", "https://www.qingting.fm", "网络音频聚合平台", "#29B6F3"),
    ("荔枝FM", "https://www.lizhi.fm", "人人都是主播", "#FF8C00"),
    ("猫耳FM", "https://www.missevan.com", "二次元声优社区", "#E91E63"),
    ("懒人听书", "https://www.lrts.me", "有声阅读平台", "#1E88E5"),
    ("波点音乐", "https://www.bodianmusic.com", "年轻化音乐App", "#7C4DFF"),
    ("汽水音乐", "https://d.qianqian.com", "字节跳动音乐App", "#00D6F9"),
    ("MOO音乐", "https://moo.music", "小众音乐发现工具", "#000000"),
    ("Echo回声", "https://app.echo.cn", "音乐故事分享社区", "#1976D2"),
    ("音悦Tai", "https://www.yinyuetai.com", "高清MV播放平台", "#FF0036"),
    ("Billboard公告牌", "https://www.billboard.com", "美国音乐排行榜", "#00AEEF"),
    ("Rolling Stone滚石", "https://www.rollingstone.com", "传奇音乐杂志", "#E01A22"),
    ("Pitchfork", "https://pitchfork.com", "独立音乐评测媒体", "#EB0000"),
    ("Genius歌词库", "https://genius.com", "全球最大歌词数据库", "#FFFF64"),
    ("MusicBrainz", "https://musicbrainz.org", "开源音乐元数据库", "#BAAB89"),
    ("Last.fm", "https://www.last.fm", "音乐社交与推荐", "#D51007"),
    ("Discogs", "https://www.discogs.com", "全球唱片数据库", "#333333"),
    ("AllMusic", "https://www.allmusic.com", "全面音乐资料库", "#EF3E42"),
    ("BandLab", "https://www.bandlab.com", "在线音乐制作协作", "#FF4B4B"),
    ("Soundation", "https://soundation.com", "在线音乐制作工作室", "#1DB954"),
    ("Amped Studio", "https://ampedstudio.com", "云端DAW工作站", "#FF6B35"),
    ("Soundtrap", "https://soundtrap.com", "Spotify在线编曲工具", "#1DB954"),
    ("GarageBand", "https://www.apple.com/mac/garageband/", "苹果免费音乐制作", "#007AFF"),
    ("Audacity", "https://www.audacityteam.org", "开源免费音频编辑器", "#000000"),
    ("OBS Studio", "https://obsproject.com", "开源录屏直播软件", "#302E31"),
    ("Vocaloid", "https://www.vocaloid.com", "歌声合成引擎软件", "#00BCD4"),
    ("MuseScore", "https://musescore.org", "免费乐谱编辑软件", "#1A80B4"),
    ("虫虫钢琴", "https://www.gangqinpu.com", "钢琴曲谱下载平台", "#4CAF50"),
    ("简谱吧", "https://www.jianpu8.com", "简谱分享交流社区", "#FF5722"),
    ("QQ音乐电台", "https://y.qq.com/n/ryqq/radio", "QQ音乐网络电台", "#31C27C"),
]

FINANCE_SITES = [
    # Main page top 5
    ("东方财富", "https://www.eastmoney.com", "财经股票门户", "#E53935"),
    ("同花顺", "https://www.10jqka.com.cn", "投资理财平台", "#E53935"),
    ("雪球", "https://xueqiu.com", "投资者交流社区", "#1E88E5"),
    ("天天基金", "https://fund.eastmoney.com", "基金交易平台", "#E53935"),
    ("蚂蚁财富", "https://fund.alibaba.com", "蚂蚁金服理财平台", "#1677FF"),
    # Additional 45+
    ("富途牛牛", "https://www.futunn.com", "港美股投资交易", "#1677FF"),
    ("老虎证券", "https://www.itiger.com", "全球投资交易平台", "#FF6B00"),
    ("长桥证券", "https://www.longbridgeapp.com", "新一代港美股券商", "#1890FF"),
    ("华盛通", "https://www.hstong.com", "华盛证券交易APP", "#FF6600"),
    ("艾德一站通", "https://www.eddid.com.hk", "艾德证券期货", "#E65100"),
    ("新浪财经", "https://finance.sina.com.cn", "新浪财经频道", "#E53935"),
    ("搜狐财经", "https://business.sohu.com", "搜狐财经频道", "#E53935"),
    ("网易财经", "https://money.163.com", "网易财经频道", "#C62828"),
    ("腾讯财经", "https://finance.qq.com", "腾讯财经频道", "#1E88E5"),
    ("金融界", "https://www.jrj.com.cn", "财经证券资讯", "#E53935"),
    ("和讯网", "https://www.hexun.com", "财经金融信息平台", "#E53935"),
    ("第一财经", "https://www.yicai.com", "专业财经媒体", "#E65100"),
    ("财新网", "https://www.caixin.com", "财经新闻专业媒体", "#0D47A1"),
    ("华尔街见闻", "https://wallstreetcn.com", "全球财经即时通讯", "#212121"),
    ("格隆汇", "https://www.gelonghui.com", "海外投资研究平台", "#1E88E5"),
    ("智通财经", "https://www.zhitongcaijing.com", "港股资讯服务平台", "#FF6600"),
    ("中国基金报", "https://www.chnfund.com", "基金行业权威媒体", "#E53935"),
    ("私募排排网", "https://www.simuwang.com", "私募基金数据平台", "#1565C0"),
    ("好买基金", "https://www.fundhowbuy.com", "第三方基金销售平台", "#E53935"),
    ("蛋卷基金", "https://danjuanfunds.com", "雪球旗下基金平台", "#1E88E5"),
    ("且慢", "https://qieman.com", "基金组合跟投平台", "#FF6B00"),
    ("普益基金", "https://www.pufund.com", "智能投顾理财平台", "#1E88E5"),
    ("京东金融", "https://jr.jd.com", "京东数字科技平台", "#E4393C"),
    ("度小满金融", "https://www.duxiaoman.com", "百度旗下金融科技", "#2932E1"),
    ("360借条", "https://www.360jieju.com", "360信用借款服务", "#21A3DD"),
    ("微粒贷", "https://weilidai.qq.com", "微信小额贷款服务", "#07C160"),
    ("借呗", "https://jiebei.alipay.com", "支付宝消费信贷", "#1677FF"),
    ("花呗", "https://huabei.alipay.com", "蚂蚁消费信贷产品", "#1677FF"),
    ("招商银行", "https://www.cmbchina.com", "零售银行领先者", "#E53935"),
    ("工商银行", "https://www.icbc.com.cn", "中国最大商业银行", "#C62828"),
    ("建设银行", "https://www.ccb.com", "国有大型商业银行", "#0066B3"),
    ("中国银行", "https://www.boc.cn", "国际化程度最高银行", "#BF360C"),
    ("农业银行", "https://www.abchina.com", "四大行之一", "#009E40"),
    ("交通银行", "https://www.bankcomm.com", "国有股份制银行", "#002C5F"),
    ("平安银行", "https://bank.pingan.com", "综合金融服务集团", "#FF6600"),
    ("浦发银行", "https://www.spdb.com.cn", "全国性股份制银行", "#1E3A6E"),
    ("兴业银行", "https://www.cib.com.cn", "绿色金融先行者", "#004098"),
    ("微众银行", "https://webank.com", "首家互联网银行", "#1E88E5"),
    ("网商银行", "https://www.mybank.cn", "蚂蚁集团旗下银行", "#FF6A00"),
    ("众安保险", "https://www.zhongan.com", "互联网保险公司", "#FF6600"),
    ("水滴筹", "https://www.shuidichou.com", "大病筹款平台", "#1E88E5"),
    ("轻松筹", "https://www.qschou.com", "大病互助众筹平台", "#FF6B00"),
    ("企查查", "https://www.qcc.com", "企业信息查询平台", "#2962FF"),
    ("天眼查", "https://www.tianyancha.com", "商业查询平台", "#2F54EB"),
    ("启信宝", "https://www.qixin.com", "企业征信查询工具", "#1E88E5"),
    ("Wind万得", "https://www.wind.com.cn", "金融数据终端", "#E53935"),
    ("Choice金融终端", "https://choice.eastmoney.com", "东方财富数据终端", "#E53935"),
]

LIFE_SITES = [
    # Main page top 5
    ("美团", "https://www.meituan.com", "吃喝玩乐全覆盖", "#FFC300"),
    ("大众点评", "https://www.dianping.com", "本地生活服务", "#FF6000"),
    ("饿了么", "https://www.ele.me", "外卖订餐平台", "#0090FF"),
    ("58同城", "https://www.58.com", "分类信息生活平台", "#FF552E"),
    ("携程旅行", "https://www.ctrip.com", "一站式旅游服务", "#2590D9"),
    # Additional 45+
    ("去哪儿旅行", "https://www.qunar.com", "机票酒店比价预订", "#3F86E9"),
    ("飞猪旅行", "https://www.fliggy.com", "阿里巴巴旗下旅行", "#FF5000"),
    ("同程旅行", "https://www.ly.com", "一站式出行平台", "#FF6B00"),
    ("马蜂窝", "https://www.mafengwo.cn", "旅游攻略与预订", "#FF9D00"),
    ("途家民宿", "https://www.tujia.com", "精品民宿预订平台", "#FF6600"),
    ("Airbnb爱彼迎", "https://www.airbnb.cn", "全球短租民宿平台", "#FF5A5F"),
    ("Booking缤客", "https://www.booking.com", "全球酒店预订平台", "#003580"),
    ("Agoda安可达", "https://www.agoda.com", "亚洲酒店预订专家", "#1A92CB"),
    ("TripAdvisor猫途鹰", "https://www.tripadvisor.cn", "全球旅游点评社区", "#00AF87"),
    ("智行火车票", "https://www.zxing.cn", "火车票抢票神器", "#1E88E5"),
    ("12306官网", "https://www.12306.cn", "铁路官方购票平台", "#E53935"),
    ("航旅纵横", "https://www.umetrip.com", "航班动态查询", "#1565C0"),
    ("高德地图", "https://www.amap.com", "数字地图内容导航", "#F9841E"),
    ("百度地图", "https://map.baidu.com", "智能路线规划导航", "#3385FF"),
    ("腾讯地图", "https://map.qq.com", "精准导航出行服务", "#00B96B"),
    ("滴滴出行", "https://www.didiglobal.com", "一站式出行平台", "#FF6A00"),
    ("高德打车", "https://damap.amap.com", "高德旗下网约车", "#F9841E"),
    ("T3出行", "https://www.t3go.com.cn", "车联网出行平台", "#1E88E5"),
    ("哈啰出行", "https://www.hellobike.com", "共享单车+顺风车", "#18A84B"),
    ("美团打车", "https://waimai.meituan.com", "美团网约车服务", "#FFC300"),
    ("货拉拉", "https://www.huolala.cn", "同城货运搬家平台", "#00C0F3"),
    ("快狗打车", "https://www.sogou.com/kuaigou", "拉货搬家服务平台", "#FF6600"),
    ("丰巢快递柜", "https://fcbox.com", "智能快递寄取服务", "#FF6600"),
    ("菜鸟裹裹", "https://www.cainiao.com", "菜鸟物流查询", "#1A73E8"),
    ("顺丰速运", "https://www.sf-express.com", "顺丰快递查询寄件", "#E53935"),
    ("中通快递", "https://www.zto.com", "中通快递单号查询", "#FF6B00"),
    ("圆通速递", "https://www.yto.net.cn", "圆通快递查询", "#1E88E5"),
    ("韵达快递", "https://www.yundaex.com", "韵达快递单号追踪", "#E53935"),
    ("申通快递", "https://www.sto.cn", "申通快递查询服务", "#E53935"),
    ("邮政EMS", "https://www.ems.com.cn", "中国邮政特快专递", "#1E88E5"),
    ("叮咚买菜", "https://www.ddmall.com", "生鲜电商配送", "#00B365"),
    ("每日优鲜", "https://www.meiguoyixian.com", "生鲜O2O平台", "#4CAF50"),
    ("盒马鲜生", "https://www.freshippo.com", "新零售生鲜超市", "#00A0E9"),
    ("永辉生活", "https://www.yonghui.com.cn", "永辉线上购物", "#E53935"),
    ("大润发优鲜", "https://e.rt-mart.com.cn", "大润发线上商城", "#E53935"),
    ("山姆会员商店", "https://www.samsclub.cn", "高端会员制超市", "#E53935"),
    ("Costco开市客", "https://www.costco.com.cn", "会员制仓储超市", "#0064B8"),
    ("美团优选", "https://www.meituan.com", "美团社区团购", "#FFC300"),
    ("多多买菜", "https://pinduoduo.com", "拼多多社区团购", "#E02E24"),
    ("贝壳找房", "https://www.ke.com", "品质居住服务平台", "#00AE66"),
    ("链家", "https://www.lianjia.com", "房产经纪服务平台", "#E53935"),
    ("安居客", "https://www.anjuke.com", "房产信息搜索平台", "#E53935"),
    ("自如", "https://www.ziroom.com", "品质租房平台", "#FF6B00"),
    ("巴乐兔租房", "https://www.baletoo.com", "年轻人租房平台", "#FF6600"),
    ("青客公寓", "https://www.qk365.com", "品牌长租公寓", "#1E88E5"),
    ("中华英才网", "https://www.chinahr.com", "专业招聘求职平台", "#E53935"),
    ("前程无忧51job", "https://www.51job.com", "综合求职招聘网站", "#E53935"),
    ("BOSS直聘", "https://www.zhipin.com", "直聘模式找工作", "#00BEAF"),
    ("猎聘", "https://www.liepin.com", "中高端人才求职", "#1E88E5"),
    ("拉勾网", "https://www.lagou.com", "互联网求职招聘", "#00B388"),
    ("脉脉职场", "https://maimai.cn", "职场社交实名平台", "#1E88E5"),
    ("实习僧", "https://www.shixiseng.com", "大学生实习招聘平台", "#FF6B00"),
    ("斗米兼职", "https://www.doumi.com", "灵活用工兼职平台", "#FF6600"),
]

# Category config: (slug, title, subtitle, icon_color, css_var, data)
CATEGORIES = [
    ("video", "视频网站", "短视频 · 直播 · 影视 · 演出", "#EF4444", "cat-video", VIDEO_SITES),
    ("knowledge", "知识网站", "学术 · 教育 · 编程 · 科普", "#10B981", "cat-knowledge", KNOWLEDGE_SITES),
    ("literature", "文学网站", "小说 · 阅读 · 散文 · 诗歌", "#F59E0B", "cat-literature", LITERATURE_SITES),
    ("news", "资讯网站", "新闻 · 财经 · 科技 · 体育", "#EF4444", "cat-news", NEWS_SITES),
    ("shop", "电商网站", "购物 · 海淘 · 生鲜 · 特卖", "#8B5CF6", "cat-shop", SHOP_SITES),
    ("game", "游戏网站", "主机 · 手游 · 单机 · 电竞", "#10B981", "cat-game", GAME_SITES),
    ("tool", "工具与设计", "效率 · 开发 · 设计 · 协作", "#06B6D4", "cat-tool", TOOL_DESIGN_SITES),
    ("music", "音乐网站", "在线听歌 · 音乐社区 · 音频平台", "#EC4899", "cat-music", MUSIC_SITES),
    ("finance", "金融理财", "股票 · 基金 · 银行 · 保险", "#F59E0B", "cat-finance", FINANCE_SITES),
    ("life", "生活服务", "外卖 · 出行 · 旅游 · 租房", "#10B981", "cat-life", LIFE_SITES),
]


def generate_page(slug, title, subtitle, icon_color, css_var, sites):
    """Generate a single secondary page HTML."""

    site_count = len(sites)
    cards_html = ""
    for name, url, desc, color in sites:
        cards_html += f'''      <a class="site-card" href="{url}" target="_blank" rel="noopener">
        <div class="brand-color" style="background: {color};"></div>
        <div class="site-info"><span class="site-name">{name}</span><span class="site-desc">{desc}</span></div>
      </a>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - luobox</title>

<!-- SEO Meta -->
<meta name="description" content="luobox {title}分类导航，收录{site_count}个精选{title}，包括{subtitle}。一键直达常用网站。">
<meta name="keywords" content="luobox,{title},网址导航,{subtitle}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://luobox.example.com/{slug}.html">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title} - luobox 导航">
<meta property="og:description" content="{title}分类收录{site_count}个精选网站，一键直达。">

<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='8' fill='%232563EB'/><path d='M2 16c2-4 4-6 7-6s3 4 6 4 5-2 7-4c0 6-4 12-10 12S5 20 2 16z' fill='white'/></svg>">

<style>
/* ========== CSS Reset & Variables ========== */
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

:root {{
  --primary: #2563EB;
  --primary-dark: #1D4ED8;
  --text-primary: #0F172A;
  --text-secondary: #64748B;
  --bg-white: #FFFFFF;
  --bg-search: #F0F4F8;
  --bg-subtle: #F8FAFC;
  --cat-color: {icon_color};
  --page-width: 1200px;
  --content-padding: 48px;
}}

body {{
  font-family: 'Sarasa Gothic SC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-subtle);
  color: var(--text-primary);
  min-height: 100vh;
}}

/* ========== Header ========== */
.header {{
  width: 100%;
  height: 64px;
  background: var(--bg-white);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--content-padding);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(148, 163, 184, 0.12);
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}}

.logo-area {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}}

.logo-icon {{
  width: 28px; height: 28px;
  background: var(--primary);
  border-radius: 7px;
  display: flex; align-items: center; justify-content: center;
}}
.logo-icon svg {{ width: 14px; height: 14px; }}

.logo-text {{
  font-size: 17px; font-weight: 700; color: var(--text-primary); letter-spacing: -0.3px;
}}

.header-search {{
  width: 400px; height: 40px;
  background: var(--bg-search);
  border-radius: 20px;
  display: flex; align-items: center;
  padding: 0 14px; gap: 8px;
  border: 1.5px solid transparent;
  transition: border-color 0.2s, box-shadow 0.2s;
}}
.header-search:focus-within {{
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37,99,235,0.08);
}}
.header-search input {{
  flex: 1; border: none; outline: none;
  font-size: 13px; font-family: inherit; color: var(--text-primary); background: transparent;
}}
.header-search input::placeholder {{ color: #94A3B8; }}
.search-icon-btn {{
  width: 26px; height: 26px; border: none; background: transparent; cursor: pointer;
  display: flex; align-items: center; justify-content: center; border-radius: 50%;
  color: #94A3B8; padding: 0; transition: background 0.15s;
}}
.search-icon-btn:hover {{ background: rgba(37,99,235,0.06); color: var(--primary); }}

.breadcrumb {{
  display: flex; align-items: center; gap: 6px;
  font-size: 13px; color: var(--text-secondary);
}}
.breadcrumb a {{ text-decoration: none; color: var(--primary); }}
.breadcrumb a:hover {{ text-decoration: underline; }}
.breadcrumb .sep {{ color: #CBD5E1; }}

/* ========== Category Hero ========== */
.cat-hero {{
  background: linear-gradient(135deg, {icon_color} 0%, {icon_color}dd 100%);
  padding: 56px var(--content-padding) 44px;
  color: white;
  position: relative; overflow: hidden;
}}
.cat-hero::before {{
  content: '';
  position: absolute; top: -40%; right: -15%;
  width: 700px; height: 700px;
  background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}}
.cat-hero-inner {{ position: relative; z-index: 1; max-width: var(--page-width); margin: 0 auto; }}
.cat-icon-large {{
  width: 48px; height: 48px; border-radius: 12px;
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(8px);
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 16px;
}}
.cat-hero h1 {{
  font-size: 32px; font-weight: 800; letter-spacing: 0.5px; margin-bottom: 8px;
}}
.cat-hero .cat-subtitle {{
  font-size: 16px; opacity: 0.9; font-weight: 400;
}}
.cat-stats {{
  display: flex; gap: 32px; margin-top: 24px;
}}
.stat-item .num {{ font-size: 28px; font-weight: 800; }}
.stat-item .label {{ font-size: 13px; opacity: 0.8; margin-top: 2px; }}

/* ========== Filter Bar ========== */
.filter-bar {{
  max-width: var(--page-width); margin: -24px auto 0;
  background: var(--bg-white); border-radius: 12px;
  padding: 14px 24px;
  display: flex; align-items: center; gap: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  position: relative; z-index: 2;
}}
.filter-bar .search-input {{
  flex: 1; height: 38px;
  border: 1.5px solid #E2E8F0; border-radius: 10px;
  padding: 0 14px; font-size: 14px;
  transition: border-color 0.2s; outline: none;
  font-family: inherit; color: var(--text-primary);
}}
.filter-bar .search-input:focus {{ border-color: var(--cat-color); }}
.filter-bar .search-input::placeholder {{ color: #94A3B8; }}
.count-badge {{
  font-size: 13px; color: var(--text-secondary); white-space: nowrap;
}}
.count-badge strong {{ color: var(--cat-color); font-weight: 700; }}

/* ========== Content ========== */
.content-area {{
  max-width: var(--page-width); margin: 0 auto;
  padding: 32px var(--content-padding) 64px;
}}

.card-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 14px;
}}

.site-card {{
  display: flex; align-items: center; gap: 14px;
  padding: 16px 18px;
  background: var(--bg-white);
  border: 1.5px solid rgba(148,163,184,0.12);
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s cubic-bezier(0.4,0,0.2,1);
  cursor: pointer;
}}
.site-card:hover {{
  transform: translateY(-2px);
  border-color: var(--cat-color);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}}
.brand-color {{
  width: 42px; height: 42px;
  min-width: 42px;
  border-radius: 10px;
  flex-shrink: 0;
}}
.site-info {{
  display: flex; flex-direction: column; gap: 3px;
  overflow: hidden; min-width: 0;
}}
.site-name {{
  font-size: 15px; font-weight: 600; color: var(--text-primary);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.site-desc {{
  font-size: 12.5px; font-weight: 400; color: var(--text-secondary);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}

/* ========== Footer ========== */
.footer {{
  background: #F8FAFC;
  border-top: 1px solid rgba(148,163,184,0.12);
  padding: 32px var(--content-padding);
  text-align: center;
}}
.footer-links {{
  display: flex; justify-content: center; gap: 24px; margin-bottom: 16px;
}}
.footer-links a {{
  font-size: 13px; color: var(--text-secondary); text-decoration: none;
}}
.footer-links a:hover {{ color: var(--primary); }}
.footer-copy {{
  font-size: 12px; color: #94A3B8;
}}

/* ========== No-results message ========== */
.no-results {{
  grid-column: 1 / -1;
  text-align: center; padding: 48px 0;
  color: var(--text-secondary); font-size: 15px;
}}

/* ========== Responsive ========== */
@media (max-width: 768px) {{
  .card-grid {{ grid-template-columns: 1fr; }}
  .header {{ padding: 0 16px; }}
  .content-area {{ padding: 24px 16px 48px; }}
  .cat-hero {{ padding: 40px 16px 32px; }}
  .cat-hero h1 {{ font-size: 26px; }}
  .filter-bar {{ padding: 10px 16px; flex-wrap: wrap; }}
}}
</style>
</head>
<body>

<!-- ===== Header ===== -->
<header class="header">
  <a href="index.html" class="logo-area">
    <div class="logo-icon">
      <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2 12C4 8 6 6 9 6C12 6 12 10 15 10C18 10 20 8 22 6C22 12 18 18 12 18C8 18 5 16 2 12Z" fill="white"/>
        <path d="M2 16C4 14 6 13 9 13C12 13 12 16 15 16C18 16 20 14 22 12" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    <span class="logo-text">luobox</span>
  </a>
  <div style="display:flex;align-items:center;gap:20px;">
    <nav class="breadcrumb">
      <a href="index.html">首页</a>
      <span class="sep">/</span>
      <span>{title}</span>
    </nav>
    <div class="header-search">
      <input type="text" placeholder="搜索此分类..." id="headerSearchInput" autocomplete="off">
      <button class="search-icon-btn" onclick="doHeaderSearch()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="6" stroke="currentColor" stroke-width="2"/><path d="M15 15L19 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>

<!-- ===== Category Hero ===== -->
<section class="cat-hero">
  <div class="cat-hero-inner">
    <div class="cat-icon-large">
      <!-- Category-specific icon placeholder -->
      <svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="3" y="3" width="18" height="18" rx="4" stroke="white" stroke-width="2"/>
        <path d="M8 8h8M8 12h8M8 16h5" stroke="white" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </div>
    <h1>{title}</h1>
    <p class="cat-subtitle">{subtitle}</p>
    <div class="cat-stats">
      <div class="stat-item">
        <div class="num">{site_count}</div>
        <div class="label">收录网站</div>
      </div>
      <div class="stat-item">
        <div class="num">TOP 5</div>
        <div class="label">首页推荐</div>
      </div>
      <div class="stat-item">
        <div class="num">实时</div>
        <div class="label">持续更新</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== Filter Bar ===== -->
<div class="filter-bar">
  <input type="text" class="search-input" placeholder="在 {title} 中搜索..." id="filterInput" autocomplete="off">
  <span class="count-badge">共 <strong id="visibleCount">{site_count}</strong> 个网站</span>
</div>

<!-- ===== Content Area ===== -->
<main class="content-area">
  <div class="card-grid" id="cardGrid">
{cards_html}
  </div>
</main>

<!-- ===== Footer ===== -->
<footer class="footer">
  <div class="footer-links">
    <a href="index.html">返回首页</a>
    <a href="{slug}.html">刷新列表</a>
  </div>
  <div class="footer-copy">2026 luobox · 收录互联网精彩站点</div>
</footer>

<script>
// ===== Search Engine Config =====
const SEARCH_ENGINES = {{
  baidu: {{ name: '百度', url: 'https://www.baidu.com/s?wd=', icon: '🔍' }},
  google: {{ name: 'Google', url: 'https://www.google.com/search?q=', icon: '🌐' }},
  bing: {{ name: 'Bing', url: 'https://www.bing.com/search?q=', icon: '🔎' }}
}};
let currentEngine = 'baidu';

function doHeaderSearch() {{
  const q = document.getElementById('headerSearchInput').value.trim();
  if (!q) return;
  window.open(SEARCH_ENGINES[currentEngine].url + encodeURIComponent(q), '_blank');
}}

document.getElementById('headerSearchInput').addEventListener('keydown', e => {{
  if (e.key === 'Enter') doHeaderSearch();
}});

// ===== In-page Filter Search =====
const filterInput = document.getElementById('filterInput');
const cardGrid = document.getElementById('cardGrid');
const allCards = Array.from(cardGrid.querySelectorAll('.site-card'));
const countBadge = document.getElementById('visibleCount');

filterInput.addEventListener('input', () => {{
  const keyword = filterInput.value.trim().toLowerCase();
  let visible = 0;

  allCards.forEach(card => {{
    const name = card.querySelector('.site-name')?.textContent.toLowerCase() || '';
    const desc = card.querySelector('.site-desc')?.textContent.toLowerCase() || '';

    if (!keyword || name.includes(keyword) || desc.includes(keyword)) {{
      card.style.display = '';
      visible++;
    }} else {{
      card.style.display = 'none';
    }}
  }});

  countBadge.textContent = visible;

  // Show no results message
  let noResults = document.querySelector('.no-results');
  if (visible === 0 && !noResults) {{
    const div = document.createElement('div');
    div.className = 'no-results';
    div.textContent = '没有找到匹配的网站，换个关键词试试';
    cardGrid.appendChild(div);
  }} else if (visible > 0 && noResults) {{
    noResults.remove();
  }}
}});
</script>

</body>
</html>'''

    filepath = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] {filepath} — {site_count} sites")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for slug, title, sub, color, _, sites in CATEGORIES:
        generate_page(slug, title, sub, color, _, sites)
    print(f"\nDone! Generated {len(CATEGORIES)} pages.")


if __name__ == "__main__":
    main()
