# 麻将与概率

一提到“做牌”，很多人第一反应是：

“这手该做什么役？”

但如果把麻将的本质抓得更准一些，就会发现这不是最核心的问题。

## 做牌的本质是什么

一副完整和牌手，归根到底是：

**四组面子 + 一组雀头**

如果把麻将先当成单局内的竞争来看，本质上就是：

**四个人里，谁最先把“四面子一雀头”做完整。**

当然，最后决定胜负的是点数，而不是单纯谁先和牌。但在现代麻将里，宝牌、赤牌、祝仪等因素会大幅放大“速度”的价值。很多时候，就算没有特别漂亮的手役，只要你先把牌做成，一样能拿到很可观的收益。

所以这里最重要的认识是：

1. 麻将当然有手役
2. 但做牌的核心不是先想“我要做什么役”
3. 而是先想“我怎么更快把形做完整”

而围绕这个问题展开的，就是牌效率和概率。

## 例题 1：切哪张更容易和牌

<img src="../hai/man7.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/man8.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou1.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou2.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou3.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin1.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin3.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 碰<img src="../hai/tyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/ytyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="32" height="24" /><img src="../hai/tyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 自摸<img src="../hai/man9.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />

这手里，三组面子和雀头都已经差不多成型，只差最后一组面子。

如果切 <img src="../hai/pin1.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />，那么只要摸到或荣和 <img src="../hai/pin2.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />、<img src="../hai/pin5.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 就能和牌。

如果切 <img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />，则基本只剩等 <img src="../hai/pin2.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 这一类机会。

哪边更容易和牌，其实不用算得太细，直觉就能看出来：受入种类更多的一边当然更优。

## 例题 2：种类一样，枚数不一样

<img src="../hai/man7.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/man8.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou1.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou2.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou3.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin3.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 碰<img src="../hai/tyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /><img src="../hai/ytyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="32" height="24" /><img src="../hai/tyun.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 自摸<img src="../hai/man9.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />

这手更有代表性。

听牌候选是切 <img src="../hai/pin3.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" /> 或切 <img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px;" width="24" height="34" />。

表面看，两边都是等两种牌，似乎差不多。但实际上差很多：

1. 如果保留的是自己已经大量使用过的牌型，那么场上剩余枚数会减少
2. 如果保留的是自己还没压缩掉太多的牌型，那么剩余枚数就更多

也就是说，麻将不能只看“有几种受入”，还要看“每种受入还剩多少枚”。

原页这张图表达的就是这个意思：

<img src="../images/003a.gif" style="display:inline; vertical-align:middle; margin:0 1px;" />

所以，做牌时真正该养成的基本习惯是：

**选择那种能让自己以更高概率抽中和牌牌的打牌。**

这就是牌效率最基础的出发点。

## 不要被单次结果带着走

麻将在初学阶段最容易犯的错误之一，就是用一次结果去否定长期正确选择。

比如你按牌效率切牌后，结果后来另一边的牌先出来了，于是你就会后悔：“早知道刚才切另一张。”

这种想法很危险，因为它会把你带回结果论。

麻将是一个高波动游戏。即使你做了长期最优选择，短期也完全可能输；反过来，就算你做了明显亏损选择，也经常会“刚好成了”。

因此，真正应该问的不是：

“这一次结果好不好？”

而是：

**“如果把这种选择重复很多次，哪边整体更赚？”**

## 这一页的结论

1. 做牌的核心，是更快完成“四面子一雀头”
2. 牌效率本质上是概率问题
3. 选择打牌时，要优先保留受入更多、枚数更大的路线
4. 不要用单次结果否定长期正确选择

下一步，就会进入更细的内容：听牌、向听，以及牌形本身到底该怎么拆、怎么理解。

---

原始日文页：<http://beginners.biz/kihon/kihon02.html>
