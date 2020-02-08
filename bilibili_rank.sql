/*
 Navicat Premium Data Transfer

 Source Server         : K1
 Source Server Type    : MariaDB
 Source Server Version : 100144
 Source Host           : localhost:3306
 Source Schema         : bilibili_rank

 Target Server Type    : MariaDB
 Target Server Version : 100144
 File Encoding         : 65001

 Date: 08/02/2020 13:37:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rank_list
-- ----------------------------
DROP TABLE IF EXISTS `rank_list`;
CREATE TABLE `rank_list`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `visit` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `up` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `up_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `av_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `get_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of rank_list
-- ----------------------------
INSERT INTO `rank_list` VALUES (1, '1', '做好防护，走出家门，大sao为远方的朋友做了一顿特殊的炸鸡腿', '7421625', '284.4万', '徐大sao', '390461123', 'av87339507', 'https://www.bilibili.com/video/av87339507', '2020-02-08 13:26:43');
INSERT INTO `rank_list` VALUES (2, '2', '祖 安 司 机', '3399602', '312.5万', '逗比的雀巢', '5294454', 'av86849641', 'https://www.bilibili.com/video/av86849641', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (3, '3', '看完这个视频你会爱上数学的！！！', '3166874', '273.5万', '帕诺雾哒哒', '503159337', 'av86478090', 'https://www.bilibili.com/video/av86478090', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (4, '4', '我竟然上电视了！【阅片无数33】', '3043405', '369.9万', '凉风Kaze', '14110780', 'av86888362', 'https://www.bilibili.com/video/av86888362', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (5, '5', '【抗肺炎】村长硬核广播trap《贱》', '2981431', '143.4万', 'OELoop', '6171645', 'av85965831', 'https://www.bilibili.com/video/av85965831', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (6, '6', '【半佛】瑞幸咖啡是如何暴打资本主义的？', '2690110', '169.3万', '硬核的半佛仙人', '37663924', 'av86712358', 'https://www.bilibili.com/video/av86712358', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (7, '7', '连续爆肝45天用方块还原拜年祭？【火锅城】完美细节还原！', '2582129', '142.8万', '国家建筑师Cthuwork', '24323', 'av86961392', 'https://www.bilibili.com/video/av86961392', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (8, '8', '10万口罩从海外送到中国有多难？1吨医疗物资送往黄冈全记录', '2521007', '114.7万', '歪果仁研究协会', '32820037', 'av86799858', 'https://www.bilibili.com/video/av86799858', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (9, '9', '【泪腺崩坏】RAM WIRE - 尽管我们的手中空无一物，【中日字幕】', '2375817', '30.2万', '時ノ舞', '374585', 'av2361621', 'https://www.bilibili.com/video/av2361621', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (10, '10', '我们，鬼畜区，向冠状病毒宣战！', '2325996', '96.5万', '无尽の零', '305214791', 'av86158890', 'https://www.bilibili.com/video/av86158890', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (11, '11', '【处处吻】 愣着干嘛 进来白嫖啊', '2157369', '105.7万', '一本正经的小方', '400413571', 'av82766716', 'https://www.bilibili.com/video/av82766716', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (12, '12', '冰块奏鸣曲', '2153488', '158.6万', '十五的月亮廿九圆', '397211154', 'av86535997', 'https://www.bilibili.com/video/av86535997', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (13, '13', '一代“国漫之光”《知音漫客》是如何衰落的？这些漫画有陪伴你的童年吗？', '2111605', '150.3万', '烟花君Ga', '357259310', 'av86691885', 'https://www.bilibili.com/video/av86691885', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (14, '14', '宅家7天，试做失传100多年的宫廷菜，把肉塞进豆芽里！', '2090661', '182.7万', '绵羊料理', '18202105', 'av86915106', 'https://www.bilibili.com/video/av86915106', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (15, '15', '武汉疫情对全职up产生的重要影响', '2063788', '84.7万', '小缸和阿灿', '37961599', 'av86969673', 'https://www.bilibili.com/video/av86969673', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (16, '16', '【哔哩哔哩2020拜年祭】', '2014075', '219.1万', '哔哩哔哩弹幕网', '8047632', 'av78976165', 'https://www.bilibili.com/video/av78976165', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (17, '17', '终于凑齐了(ಡωಡ)', '2009164', '43.7万', 'Youtube中文字幕组', '382189062', 'av86775156', 'https://www.bilibili.com/video/av86775156', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (18, '18', '【散人】全程坑爹 崩溃嚎叫的气人i wanna', '1562947', '76.4万', '逍遥散人', '168598', 'av86715254', 'https://www.bilibili.com/video/av86715254', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (19, '19', '女团腿 去头尾 自用', '1561015', '40.5万', '代号白菜君599', '248404676', 'av70455264', 'https://www.bilibili.com/video/av70455264', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (20, '20', '沙雕新闻级不要笑挑战，等级：无人生还', '1490587', '136.6万', '摩登Mod', '244440947', 'av86581989', 'https://www.bilibili.com/video/av86581989', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (21, '21', '【老番茄】史上最憨训练师(第三集)', '1476149', '100.9万', '老番茄', '546195', 'av86550398', 'https://www.bilibili.com/video/av86550398', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (22, '22', '【主播真会玩八卦篇】110：冠状病毒阴霾下，你记住了哪个瞬间？', '1461024', '78.0万', '长歌与小见见', '3682229', 'av87169582', 'https://www.bilibili.com/video/av87169582', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (23, '23', '计算机仿真程序告诉你为什么现在还没到出门的时候！！！', '1455934', '99.4万', 'Ele实验室', '481434238', 'av86478875', 'https://www.bilibili.com/video/av86478875', '2020-02-08 13:26:44');
INSERT INTO `rank_list` VALUES (24, '24', '【崩坏三】对  王  之  王  八  重  樱', '1419471', '48.0万', '黑色蝌蚪君', '87305034', 'av86902105', 'https://www.bilibili.com/video/av86902105', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (25, '25', '【互动游戏】剧情高能！七个小矮人遇害身亡，凶手是白雪公主...', '1406251', '85.9万', '打泥泥', '357229416', 'av86727918', 'https://www.bilibili.com/video/av86727918', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (26, '26', '【家有儿女】家有骚话！蝙蝠炖汤，棺材反光', '1392273', '82.5万', '红豆稀饭中', '250648682', 'av86154367', 'https://www.bilibili.com/video/av86154367', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (27, '27', '能力越大责任越大！我就是这个城市的救星！一只非常普通的鹿', '1376706', '94.0万', '中国BOY超级大猩猩', '562197', 'av86883558', 'https://www.bilibili.com/video/av86883558', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (28, '28', '【沙雕动画】因为，我是医生', '1371626', '46.8万', '冰糖葫芦没放盐', '50245973', 'av86244658', 'https://www.bilibili.com/video/av86244658', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (29, '29', '高中生物必修一（人教版）视频合集', '1366117', '49.9万', '锦城大同教育', '455710037', 'av74947403', 'https://www.bilibili.com/video/av74947403', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (30, '30', '【处处吻】你的老婆可太撩了！世界都馋她一吻', '1302435', '56.0万', '动漫唯美风', '1826871', 'av85792473', 'https://www.bilibili.com/video/av85792473', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (31, '31', '每天一遍，防止早恋！', '1288731', '99.9万', '一片叶子YE', '83785129', 'av86697667', 'https://www.bilibili.com/video/av86697667', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (32, '32', '鬼知道我看了几遍', '1259681', '66.6万', '晨空qwq', '192977398', 'av86135560', 'https://www.bilibili.com/video/av86135560', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (33, '33', '［处处吻］在?坚持30秒算我输?', '1247975', '90.4万', '欢柴犬', '494648806', 'av86361699', 'https://www.bilibili.com/video/av86361699', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (34, '34', '【田逾欢】女生如何根据脸型选发型/选对发型巧妙掩盖脸型缺陷提高颜值', '1242344', '47.1万', '田逾欢sirius', '13826185', 'av86702916', 'https://www.bilibili.com/video/av86702916', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (35, '35', '祖 安 圣 歌', '1231707', '124.3万', '霞式尖叫', '9656686', 'av86897270', 'https://www.bilibili.com/video/av86897270', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (36, '36', '建 议 改 成:全 国 人 民 现 状', '1217183', '141.7万', '提着刀的胖虎', '287529225', 'av86374157', 'https://www.bilibili.com/video/av86374157', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (37, '37', '\"有些人一旦错过就不再”', '1183312', '77.2万', '锦书致南辞', '90142376', 'av86703922', 'https://www.bilibili.com/video/av86703922', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (38, '38', '国外三折购物不香吗？海淘手拉手教学 包会！', '1176446', '34.4万', '吕政懋MaoMao', '254436446', 'av86840101', 'https://www.bilibili.com/video/av86840101', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (39, '39', '【MC建筑】在山上开洞造房~ 面朝雪景 满屋温馨', '1172282', '29.5万', 'XweetokDD', '172207', 'av86720995', 'https://www.bilibili.com/video/av86720995', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (40, '40', '新型冠状病毒有多狡猾？疫情当头,肺炎之下,病毒与人类的军备竞赛,谁能活到最后？武汉加油!', '1163014', '61.3万', '思维实验室', '14583962', 'av86052908', 'https://www.bilibili.com/video/av86052908', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (41, '41', '【蔡徐坤】仙剑鸡侠传', '1134887', '58.5万', '金色传说竹鼠', '411869738', 'av86208216', 'https://www.bilibili.com/video/av86208216', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (42, '42', '【木鱼微剧场】《请回答1988》最好的韩剧，刷N遍依然感动（P1）', '1119287', '68.3万', '木鱼水心', '927587', 'av86869317', 'https://www.bilibili.com/video/av86869317', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (43, '43', '史上最骚魔鬼套路“奥利给姐姐”教你如何让对手脑淤血', '1115404', '78.0万', '守护茶茶', '37946996', 'av86803884', 'https://www.bilibili.com/video/av86803884', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (44, '44', '在床上就可以做的20分钟特快瘦大腿操  2星期内明显见效【Coffee林芊妤】', '1092625', '31.1万', '带枪小女孩weibo', '1960460', 'av22227629', 'https://www.bilibili.com/video/av22227629', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (45, '45', '快速瘦小腿运动！摆脱萝卜腿让小腿更细长，拉伸小腿【周六野Zoey】', '1087986', '30.2万', '周六野Zoey', '62540916', 'av8879609', 'https://www.bilibili.com/video/av8879609', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (46, '46', '【1周瘦腿计划表】全腿型，最少能瘦2CM｜假期宅家瘦腿打卡合集！', '1077363', '29.3万', '马戏糍', '17901717', 'av86290811', 'https://www.bilibili.com/video/av86290811', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (47, '47', '瘦腿课表（美丽芭蕾外侧+内侧+第三套+第四套+美丽芭蕾拉伸）', '1075312', '34.0万', '普鲁士ll', '2993682', 'av50314054', 'https://www.bilibili.com/video/av50314054', '2020-02-08 13:26:45');
INSERT INTO `rank_list` VALUES (48, '48', '【神经病式配音】猜 猜 我 是 谁？', '1067477', '54.9万', '一支小暗暗', '408940191', 'av83701473', 'https://www.bilibili.com/video/av83701473', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (49, '49', '王老菊教你治疗精神病', '1040750', '82.2万', '怕上火暴王老菊', '423895', 'av86977867', 'https://www.bilibili.com/video/av86977867', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (50, '50', '三个和尚——卢本伟、PDD、旭旭宝宝主演', '1021964', '49.4万', '风云熊', '38347595', 'av86582360', 'https://www.bilibili.com/video/av86582360', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (51, '51', '当她裙里拔枪那一刻！！世界：我赌你的枪里没有子弹！', '1011803', '43.7万', '烟季', '15377173', 'av83697364', 'https://www.bilibili.com/video/av83697364', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (52, '52', '沉             底', '1008193', '31.7万', '旅淡淡', '318568697', 'av86471181', 'https://www.bilibili.com/video/av86471181', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (53, '53', '大家好，我是新人UP小徐！', '996007', '110.7万', '徐大虾咯', '13354765', 'av87024983', 'https://www.bilibili.com/video/av87024983', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (54, '54', '今     夜     妈     妈     不     在     家', '992258', '68.4万', '名人鬼', '174499858', 'av84306713', 'https://www.bilibili.com/video/av84306713', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (55, '55', '【党妹】100%诚实年度榜单！零食外卖日用家电全方位解读宅的快乐！', '986692', '72.6万', '机智的党妹', '466272', 'av86639071', 'https://www.bilibili.com/video/av86639071', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (56, '56', '☀️进来沐浴阳光！☀️记得给我Thumbs up～【伢伢】韩舞翻跳', '978868', '61.1万', '伢伢gagako', '632887', 'av86962018', 'https://www.bilibili.com/video/av86962018', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (57, '57', '【朱一旦】碰到一个人在卖口罩，张口就是3万！', '967741', '138.3万', '朱一旦的二维生活', '503569552', 'av86724612', 'https://www.bilibili.com/video/av86724612', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (58, '58', '我竟然被这样的男人撩动了？超级羞耻(*/ω＼*)', '955240', '88.2万', '隔壁班的喵会长', '21330948', 'av86873561', 'https://www.bilibili.com/video/av86873561', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (59, '59', '1995年的人民猜想21世纪的中国是什么样子', '952874', '110.1万', '射程之内皆为真理', '432925927', 'av86953773', 'https://www.bilibili.com/video/av86953773', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (60, '60', '老八：但是我拒绝（请调大音量）', '952773', '77.9万', '臭恶皮蛋', '130133670', 'av86833125', 'https://www.bilibili.com/video/av86833125', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (61, '61', '犬来八荒 | 大家好，我是成果，今天正式入驻B站了！', '942234', '134.3万', '犬来八荒w', '3345720', 'av86493657', 'https://www.bilibili.com/video/av86493657', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (62, '62', '【阿斗】这是你们要的《指环王2双塔奇兵》史诗篇章圣盔谷之战！', '942055', '61.3万', '阿斗归来了', '21837784', 'av86768165', 'https://www.bilibili.com/video/av86768165', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (63, '63', '【卢本伟】处处吻 千万填词在线催泪！', '939130', '68.6万', '奶油鸽子精', '411699052', 'av86895988', 'https://www.bilibili.com/video/av86895988', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (64, '64', '地狱空荡荡 魔鬼在人间', '937449', '81.5万', '反诈骗联盟', '314482006', 'av86696922', 'https://www.bilibili.com/video/av86696922', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (65, '65', '90岁老奶奶的无奈，眼睛还瞎掉一只，村里连理发店都没有', '934206', '75.9万', '一点爱送温暖', '457871303', 'av87065141', 'https://www.bilibili.com/video/av87065141', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (66, '66', '他师傅第一次骗他，也是最后一次骗他', '933400', '56.3万', '思齐家厨', '397744889', 'av84446348', 'https://www.bilibili.com/video/av84446348', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (67, '67', '每天只要8分钟,1周瘦5斤！|学生党上班族减肥必做高强度HIIT运动 |另附无跳动新手适用版本，无需器械！', '931263', '21.8万', '韩小四April', '369750017', 'av84120893', 'https://www.bilibili.com/video/av84120893', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (68, '68', '【严禁扩散】98%几率必胜石头剪子布的方法', '929172', '46.5万', '徊加日记', '402210326', 'av86541880', 'https://www.bilibili.com/video/av86541880', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (69, '69', '假如钟南山院士说 可 以 出 门 了！！', '915315', '72.5万', 'KILLLER绅士', '11793131', 'av86814210', 'https://www.bilibili.com/video/av86814210', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (70, '70', '有些人值得你融化', '904094', '67.6万', '小小小小盒子min', '438024647', 'av86187933', 'https://www.bilibili.com/video/av86187933', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (71, '71', '网传自制可乐的方法真的靠谱吗，没想到小伙真的做出可乐的味道', '903321', '225.2万', '翔翔大作战', '196356191', 'av86913584', 'https://www.bilibili.com/video/av86913584', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (72, '72', '小伙花693元买了一个全自动泡面机，再也不用动手泡面了！', '903178', '171.4万', '贤宝宝Baby', '3957971', 'av86915086', 'https://www.bilibili.com/video/av86915086', '2020-02-08 13:26:46');
INSERT INTO `rank_list` VALUES (73, '73', '无人机喊话劝“灌篮高手”们回家......', '900038', '118.6万', '浙江共青团', '384298638', 'av86881662', 'https://www.bilibili.com/video/av86881662', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (74, '74', '花季少女竟成宠粉狂魔!?又跳又唱这谁顶得', '893755', '57.1万', '二喵的饭', '29329085', 'av87178951', 'https://www.bilibili.com/video/av87178951', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (75, '75', '不同人眼中的武汉肺炎疫情', '887394', '105.0万', 'Kevin英语情报局', '10345615', 'av86636341', 'https://www.bilibili.com/video/av86636341', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (76, '76', '全 国 现 状', '881699', '70.5万', 'ZB龙哥', '36091511', 'av86944690', 'https://www.bilibili.com/video/av86944690', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (77, '77', '握 着 我 的 抱 枕', '875629', '78.7万', 'Thomas-Lee', '293310431', 'av86791571', 'https://www.bilibili.com/video/av86791571', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (78, '78', '试 吃 异 形', '862784', '124.6万', '大祥哥来了', '2920960', 'av86815148', 'https://www.bilibili.com/video/av86815148', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (79, '79', '油管网友：中国人都是天使吗？！', '860644', '113.3万', '非氪金玩家', '130659460', 'av86308442', 'https://www.bilibili.com/video/av86308442', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (80, '80', '一时间不知道该心疼谁', '859012', '97.1万', '大霓奈', '7560829', 'av86859262', 'https://www.bilibili.com/video/av86859262', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (81, '81', '打电话恶搞兄弟，向他告白…没想到他居然答应了…读评论#1', '854166', '74.7万', '东尼ookii', '285499073', 'av87022904', 'https://www.bilibili.com/video/av87022904', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (82, '82', '【罗汉发神经】莫名其妙的游戏 小胖胖打架~', '851758', '72.7万', '罗汉解说', '51896064', 'av86902959', 'https://www.bilibili.com/video/av86902959', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (83, '83', '华农兄弟：去镇上买点菜，路过兄弟家的竹林，顺便挖点竹笋', '849467', '175.6万', '华农兄弟', '250858633', 'av86907243', 'https://www.bilibili.com/video/av86907243', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (84, '84', '【张伟个人向】致爱情公寓最有种的男人，活的最努力的人，张伟', '847878', '39.9万', '在下伍十九', '328067049', 'av86597132', 'https://www.bilibili.com/video/av86597132', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (85, '85', '在女朋友懒人沙发里塞满100个尖叫鸡，她坐上去之后...', '847739', '147.7万', '雨哥到处跑', '147166910', 'av87122351', 'https://www.bilibili.com/video/av87122351', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (86, '86', '96%的人类会在家里偷偷干的事', '843081', '71.4万', '力元君', '19642758', 'av87027052', 'https://www.bilibili.com/video/av87027052', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (87, '87', '小伙因为挑战大胃王从来没成功过，怒买十斤草莓挑战大胃王吃播！', '840585', '115.7万', '记录生活的蛋黄派', '337521240', 'av87113349', 'https://www.bilibili.com/video/av87113349', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (88, '88', '【更新1p，告别蝴蝶袖】美丽芭蕾 天鹅臂 累断手', '838388', '40.5万', '废柴家里蹲', '3751951', 'av3534854', 'https://www.bilibili.com/video/av3534854', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (89, '89', '聊      天   鬼            才', '835839', '85.3万', 'c单薇子', '415213464', 'av86460748', 'https://www.bilibili.com/video/av86460748', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (90, '90', '大排档的炒面为什么这么好吃？大厨教你一招，在家炒也一样', '828489', '47.7万', '游厨冯马迁', '452767301', 'av87205143', 'https://www.bilibili.com/video/av87205143', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (91, '91', '祖 安 公 主', '825435', '81.8万', '-句芒-', '94476885', 'av84073301', 'https://www.bilibili.com/video/av84073301', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (92, '92', '【中字】Ballet Beautiful 美丽芭蕾第三套  瘦腿提臀', '824957', '26.1万', 'pll25586', '7937899', 'av4489689', 'https://www.bilibili.com/video/av4489689', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (93, '93', '量子力学', '823199', '89.8万', '月色行凶者', '382438063', 'av86351604', 'https://www.bilibili.com/video/av86351604', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (94, '94', '象拔蚌这种海鲜！一刀下去。。。撸成串太爽了', '810355', '92.2万', '加薪食社', '14341074', 'av86903776', 'https://www.bilibili.com/video/av86903776', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (95, '95', '对子之王卢本伟', '796860', '52.1万', '多节课', '46733369', 'av85127244', 'https://www.bilibili.com/video/av85127244', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (96, '96', '【博君一肖】「年度巨制·多情种」双向暗恋，甜虐交织 | 入戏太深，总会动情', '791689', '15.9万', '切粒粒', '27692819', 'av86783152', 'https://www.bilibili.com/video/av86783152', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (97, '97', '【当你兄弟学会了女声】一分钟摧毁兄弟的幸福！你得不到的甜蜜你兄弟也别想得到', '788847', '60.0万', '姜峰真的苟', '44688866', 'av87057157', 'https://www.bilibili.com/video/av87057157', '2020-02-08 13:26:47');
INSERT INTO `rank_list` VALUES (98, '98', '【Irony】《反语》翻唱【鹿乃】', '781912', '22.9万', '鹿乃ちゃん', '316381099', 'av86889971', 'https://www.bilibili.com/video/av86889971', '2020-02-08 13:26:48');
INSERT INTO `rank_list` VALUES (99, '99', '最强自夸王！！！！！', '778101', '49.0万', '某幻君', '1577804', 'av84887919', 'https://www.bilibili.com/video/av84887919', '2020-02-08 13:26:48');
INSERT INTO `rank_list` VALUES (100, '100', '当你发现家里有蜘蛛时', '777289', '55.6万', 'E_CAT', '8266776', 'av86909483', 'https://www.bilibili.com/video/av86909483', '2020-02-08 13:26:48');

SET FOREIGN_KEY_CHECKS = 1;
