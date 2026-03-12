# 麻将与概率

一提到麻将的做牌，可能有人会觉得重点在于“要做什么役”。  
但这其实偏离了麻将的本质。

做牌的本质，是把手牌做成“四面子一雀头”的形。  
如果把麻将看成以一局为单位的竞争，那么它本质上就是：

**四个人之中，谁能最快完成四面子一雀头。**

当然，最后评价的是持点。  
但考虑到现在的麻将里宝牌、赤牌很多，即使没有手役也常常能打出高分，所以真正的本质依然不是“役”，而是“形”。

而既然只有最先把牌形完成的人才能获得分数，那么速度就必然成为核心要求。

那么，怎样才能更快和牌呢？  
为此所需要的思考方式，就是牌效率与概率。

## 例题 1：该切哪张？

<p><img src="../hai/man7.gif" width="24" height="34"><img src="../hai/man8.gif" width="24" height="34"><img src="../hai/sou1.gif" width="24" height="34"><img src="../hai/sou2.gif" width="24" height="34"><img src="../hai/sou3.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/pin1.gif" width="24" height="34"><img src="../hai/pin3.gif" width="24" height="34"><img src="../hai/pin4.gif" width="24" height="34">　　碰<img src="../hai/tyun.gif" width="24" height="34"><img src="../hai/ytyun.gif" width="32" height="24"><img src="../hai/tyun.gif" width="24" height="34">　　　自摸<img src="../hai/man9.gif" width="24" height="34"></p>

先用最简单的例子来想。  
例 1 里，三组面子和雀头都已经完成了，所以只要再做出一组面子就可以和牌。

切 <img src="../hai/pin1.gif" width="24" height="34"> 的话，只要来（或别人打出） <img src="../hai/pin2.gif" width="24" height="34"> 和 <img src="../hai/pin5.gif" width="24" height="34"> 就能和牌。

切 <img src="../hai/pin4.gif" width="24" height="34"> 的话，只要来（或别人打出） <img src="../hai/pin2.gif" width="24" height="34"> 就能和牌。

哪种切法更容易和牌，已经很明显了。

## 例题 2：该切哪张？

<p><img src="../hai/man7.gif" width="24" height="34"><img src="../hai/man8.gif" width="24" height="34"><img src="../hai/sou1.gif" width="24" height="34"><img src="../hai/sou2.gif" width="24" height="34"><img src="../hai/sou3.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/pin3.gif" width="24" height="34"><img src="../hai/pin4.gif" width="24" height="34"><img src="../hai/pin4.gif" width="24" height="34">　　碰<img src="../hai/tyun.gif" width="24" height="34"><img src="../hai/ytyun.gif" width="32" height="24"><img src="../hai/tyun.gif" width="24" height="34">　　　　　自摸<img src="../hai/man9.gif" width="24" height="34"></p>

能够取成听牌（再差一张就和牌的状态）的打牌，是 <img src="../hai/pin3.gif" width="24" height="34"> 和 <img src="../hai/pin4.gif" width="24" height="34">。

切 <img src="../hai/pin3.gif" width="24" height="34">，就是等 <img src="../hai/sou5.gif" width="24" height="34"> 和 <img src="../hai/pin4.gif" width="24" height="34">。

切 <img src="../hai/pin4.gif" width="24" height="34">，就是等 <img src="../hai/pin2.gif" width="24" height="34"> 和 <img src="../hai/pin5.gif" width="24" height="34">。

两边看起来都是等两种牌，所以和牌难度也一样吗？其实不是。

<img src="../hai/sou5.gif" width="24" height="34"> 和 <img src="../hai/pin4.gif" width="24" height="34">，自己手里各用了两张，所以剩下的只有 4 张。

而 <img src="../hai/pin2.gif" width="24" height="34"> 和 <img src="../hai/pin5.gif" width="24" height="34">，只从自己的手里判断的话，8 张都还活着。

如果让你抽签，当然是中奖签更多的一边更划算。  
所以，取成枚数更多的 <img src="../hai/pin2.gif" width="24" height="34"> - <img src="../hai/pin5.gif" width="24" height="34"> 听牌，和牌概率自然更高。

<img src="../images/003a.gif">

<p><strong>“选择能让自己以更有利的概率去抽中和牌牌的切牌方式”</strong><br>这就是做牌最基本的思考。</p>

---

<p><img src="../hai/man7.gif" width="24" height="34"><img src="../hai/man8.gif" width="24" height="34"><img src="../hai/sou1.gif" width="24" height="34"><img src="../hai/sou2.gif" width="24" height="34"><img src="../hai/sou3.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/sou5.gif" width="24" height="34"><img src="../hai/pin3.gif" width="24" height="34"><img src="../hai/pin4.gif" width="24" height="34"><img src="../hai/pin4.gif" width="24" height="34">　　碰<img src="../hai/tyun.gif" width="24" height="34"><img src="../hai/ytyun.gif" width="32" height="24"><img src="../hai/tyun.gif" width="24" height="34">　　　自摸<img src="../hai/man9.gif" width="24" height="34"></p>

例如这里，就算切了 <img src="../hai/pin4.gif" width="24" height="34">，也还是可能先看到 <img src="../hai/sou5.gif" width="24" height="34"> 或 <img src="../hai/pin4.gif" width="24" height="34">，结果错过和牌。

但即便如此，也不要因此就想：
“早知道刚才就该切 <img src="../hai/pin3.gif" width="24" height="34"> 了。”

麻将里，就算打了坏牌，也经常会刚好碰上结果不错。

没有必要每次都被这种结果论带着走。

### 总结与定式

<p class="green">麻将是一种即使打出最优手，也经常会失败的游戏。<br />
不要因为一时的结果就大喜大悲，<br />
而是要从更长的时间尺度去判断，哪种选择整体上更划算。</p>

---

原始日文页：<http://beginners.biz/kihon/kihon02.html>

<!-- PAGE NAV START -->
<div class="page-nav" markdown="0">
  <a class="page-nav__link page-nav__link--prev" href="kihon01.html">上一节：麻将是什么</a>
  <a class="page-nav__link page-nav__link--next" href="kihon03.html">下一节：听牌与向听</a>
</div>
<!-- PAGE NAV END -->
