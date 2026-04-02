<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>金宝全能助手 Pro | Kampar Ultimate Tool</title>
    <style>
        :root {
            --primary: #6c5ce7;
            --food-red: #ff4757;
            --bazi-gold: #d35400;
            --bg: #f1f2f6;
            --card: #ffffff;
            --text: #2d3436;
        }
        @media (prefers-color-scheme: dark) {
            :root { --bg: #1e272e; --card: #2f3640; --text: #f5f6fa; }
        }
        body { font-family: -apple-system, system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; min-height: 100vh; }
        
        /* 导航栏 */
        .nav-bar { background: var(--card); display: flex; justify-content: space-around; padding: 15px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; }
        .nav-item { cursor: pointer; font-weight: bold; font-size: 0.85rem; color: #888; transition: 0.3s; padding: 8px 12px; border-radius: 15px; }
        .nav-item.active { background: var(--primary); color: white; }

        .container { padding: 20px; display: flex; justify-content: center; }
        .app-card { background: var(--card); width: 100%; max-width: 420px; padding: 25px; border-radius: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); text-align: center; display: none; animation: fadeIn 0.4s ease; box-sizing: border-box; }
        .app-card.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } }

        /* 输入框与按钮 */
        input, select { width: 100%; padding: 12px; margin: 8px 0; border: 2px solid #eee; border-radius: 12px; background: var(--bg); color: var(--text); box-sizing: border-box; font-size: 1rem; }
        .main-btn { width: 100%; padding: 16px; border: none; border-radius: 15px; color: white; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 15px; }
        
        /* 八字排盘样式 */
        .bazi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 20px; }
        .bazi-pillar { background: #fdf2e9; border: 1px solid #e67e22; border-radius: 12px; padding: 10px 5px; }
        .pillar-label { font-size: 0.7rem; color: #a04000; margin-bottom: 5px; }
        .pillar-char { font-size: 1.4rem; font-weight: bold; color: #d35400; line-height: 1.2; }
        
        /* 美食盒样式 */
        .display-box { background: rgba(255, 71, 87, 0.05); border: 2px dashed var(--food-red); border-radius: 20px; padding: 20px; min-height: 140px; display: flex; flex-direction: column; justify-content: center; }

        .stat-bar { height: 8px; background: rgba(0,0,0,0.1); border-radius: 5px; margin-top: 15px; overflow: hidden; }
        .stat-fill { height: 100%; background: var(--primary); width: 0; transition: 1.5s; }
    </style>
</head>
<body>

    <div class="nav-bar">
        <div class="nav-item active" onclick="showApp('food', this)">🍜 美食</div>
        <div class="nav-item" onclick="showApp('astro', this)">✨ 星座</div>
        <div class="nav-item" onclick="showApp('bazi', this)">🔮 八字</div>
    </div>

    <div class="container">
        <div id="food-app" class="app-card active">
            <h2 style="color: var(--food-red);">Kampar Hunter</h2>
            <div class="display-box">
                <div id="foodName" style="font-size: 1.6rem; font-weight: 900;">Ready?</div>
                <div id="foodTip" style="font-size: 0.85rem; color: #888; margin-top: 10px;">摇一摇手机或点击按钮</div>
            </div>
            <button class="main-btn" style="background: var(--food-red);" id="pickBtn" onclick="handleFoodClick()">帮我决定！</button>
        </div>

        <div id="astro-app" class="app-card">
            <h2 style="color: var(--primary);">Horoscope</h2>
            <div style="text-align: left;">
                <label style="font-size: 0.8rem;">出生月/日 (MM-DD)</label>
                <div style="display: flex; gap: 10px;">
                    <input type="number" id="hMonth" placeholder="月">
                    <input type="number" id="hDay" placeholder="日">
                </div>
            </div>
            <button class="main-btn" style="background: var(--primary);" onclick="calcHoroscope()">查看星座</button>
            <div id="hRes" style="margin-top:20px; font-size: 1.3rem; font-weight: bold; color: var(--primary);"></div>
        </div>

        <div id="bazi-app" class="app-card">
            <h2 style="color: var(--bazi-gold);">八字排盘</h2>
            <div style="text-align: left; font-size: 0.85rem;">
                <label>出生年/月/日/时</label>
                <input type="date" id="bzDate">
                <select id="bzTime">
                    <option value="0">子时 (23:00-01:00)</option>
                    <option value="1">丑时 (01:00-03:00)</option>
                    <option value="3">寅时 (03:00-05:00)</option>
                    <option value="5">卯时 (05:00-07:00)</option>
                    <option value="7">辰时 (07:00-09:00)</option>
                    <option value="9">巳时 (09:00-11:00)</option>
                    <option value="11">午时 (11:00-13:00)</option>
                    <option value="13">未时 (13:00-15:00)</option>
                    <option value="15">申时 (15:00-17:00)</option>
                    <option value="17">酉时 (17:00-19:00)</option>
                    <option value="19">戌时 (19:00-21:00)</option>
                    <option value="21">亥时 (21:00-23:00)</option>
                </select>
            </div>
            <button class="main-btn" style="background: var(--bazi-gold);" onclick="calcBazi()">排出命盘</button>
            
            <div id="bzResult" style="display:none;">
                <div class="bazi-grid">
                    <div class="bazi-pillar"><div class="pillar-label">时柱</div><div class="pillar-char" id="p4">-</div></div>
                    <div class="bazi-pillar"><div class="pillar-label">日柱</div><div class="pillar-char" id="p3">-</div></div>
                    <div class="bazi-pillar"><div class="pillar-label">月柱</div><div class="pillar-char" id="p2">-</div></div>
                    <div class="bazi-pillar"><div class="pillar-label">年柱</div><div class="pillar-char" id="p1">-</div></div>
                </div>
                <div id="bzLuck" style="margin-top: 15px; font-size: 0.85rem; color: #e67e22;"></div>
            </div>
        </div>
    </div>

<script>
    // --- 导航 ---
    function showApp(id, btn) {
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        btn.classList.add('active');
        document.querySelectorAll('.app-card').forEach(c => c.classList.remove('active'));
        document.getElementById(id + '-app').classList.add('active');
    }

    // --- 八字排盘核心逻辑 (高度简化版干支推算法) ---
    function calcBazi() {
        const dateVal = document.getElementById('bzDate').value;
        const hour = parseInt(document.getElementById('bzTime').value);
        if(!dateVal) return alert("请选择日期");

        const d = new Date(dateVal);
        const year = d.getFullYear();
        const month = d.getMonth() + 1;
        const day = d.getDate();

        const TianGan = "甲乙丙丁戊己庚辛壬癸";
        const DiZhi = "子丑寅卯辰巳午未申酉戌亥";

        // 1. 年柱 (以1900年庚子年为基准)
        let yIdx = (year - 4) % 10;
        let yZIdx = (year - 4) % 12;
        const nian = TianGan[yIdx] + DiZhi[yZIdx];

        // 2. 月柱 (简化算法)
        let mIdx = ( (year % 5) * 2 + month + 1) % 10;
        const yue = TianGan[mIdx] + DiZhi[(month + 1) % 12];

        // 3. 日柱 (基于基准日的偏移量计算)
        const baseDate = new Date(1900, 0, 31); // 1900-01-31 是甲辰日
        let diff = Math.floor((d - baseDate) / (24*3600*1000));
        let ri = TianGan[diff % 10] + DiZhi[(diff + 4) % 12];

        // 4. 时柱
        let sIdx = ( (diff % 5) * 2 + Math.floor((hour+1)/2) ) % 10;
        const shi = TianGan[sIdx] + DiZhi[Math.floor((hour+1)/2) % 12];

        // UI 显示
        document.getElementById('p1').innerText = nian[0] + '\n' + nian[1];
        document.getElementById('p2').innerText = yue[0] + '\n' + yue[1];
        document.getElementById('p3').innerText = ri[0] + '\n' + ri[1];
        document.getElementById('p4').innerText = shi[0] + '\n' + shi[1];
        document.getElementById('bzResult').style.display = 'block';
        document.getElementById('bzLuck').innerText = `命格提示：${ri[0]}木命人，生于${yue[1]}月，气场极佳！`;
    }

    // --- 星座逻辑 ---
    function calcHoroscope() {
        const m = parseInt(document.getElementById('hMonth').value);
        const d = parseInt(document.getElementById('hDay').value);
        let res = "双鱼座 (Pisces)";
        if ((m == 3 && d >= 21) || (m == 4 && d <= 19)) res = "白羊座 (Aries)";
        else if ((m == 4 && d >= 20) || (m == 5 && d <= 20)) res = "金牛座 (Taurus)";
        else if ((m == 5 && d >= 21) || (m == 6 && d <= 21)) res = "双子座 (Gemini)";
        else if ((m == 6 && d >= 22) || (m == 7 && d <= 22)) res = "巨蟹座 (Cancer)";
        else if ((m == 7 && d >= 23) || (m == 8 && d <= 22)) res = "狮子座 (Leo)";
        else if ((m == 8 && d >= 23) || (m == 9 && d <= 22)) res = "处女座 (Virgo)";
        else if ((m == 9 && d >= 23) || (m == 10 && d <= 23)) res = "天秤座 (Libra)";
        else if ((m == 10 && d >= 24) || (m == 11 && d <= 22)) res = "天蝎座 (Scorpio)";
        else if ((m == 11 && d >= 23) || (m == 12 && d <= 21)) res = "射手座 (Sagittarius)";
        else if ((m == 12 && d >= 22) || (m == 1 && d <= 19)) res = "摩羯座 (Capricorn)";
        else if ((m == 1 && d >= 20) || (m == 2 && d <= 18)) res = "水瓶座 (Aquarius)";
        document.getElementById('hRes').innerText = res;
    }

    // --- 美食猎人简版代码 ---
    let allFoods = ["游记面包鸡", "瓦煲鸡饭", "金宝糯米饭", "老街牛腩粉", "新街明记火锅"];
    let isRolling = false;
    function handleFoodClick() {
        if(isRolling) return;
        isRolling = true;
        let count = 0;
        let timer = setInterval(() => {
            document.getElementById('foodName').innerText = allFoods[Math.floor(Math.random()*allFoods.length)];
            count++;
            if(count > 20) {
                clearInterval(timer);
                isRolling = false;
                document.getElementById('foodTip').innerText = "📍 就在金宝，出发吧！";
            }
        }, 60);
    }
</script>
</body>
</html>
