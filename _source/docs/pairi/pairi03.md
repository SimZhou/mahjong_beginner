# 浮牌理论

让我们来思考，麻将 34 种牌在孤张状态下，各自到底有什么价值。

## 1. 基本牌理

任何一种牌，做成对子或刻子的概率，在 34 种牌里本质上都一样。
但如果从“容易鸣成刻子”的角度来看，字牌和靠边的牌会更占便宜。

相反，如果从组成顺子的能力来看，越靠中间的数牌越有价值。
字牌则根本不能组成顺子，只能做对子或刻子。

如果以门前做牌为前提，那么大致可以这样理解牌的面子构成能力：

**<面子构成能力>**

<img src="../hai/man3.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man6.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> ＞ <img src="../hai/man2.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man8.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> ＞ <img src="../hai/man1.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> ＞ **字牌**

图里用的是万子，不过索子、饼子当然也完全一样。总之可以先记住：**越靠中间的数牌，单张价值通常越高。**

字牌的价值则更简单。能碰出役的字牌价值高，不能成役的客风牌价值低。大致可以理解为：

**双东 / 双南 ＞ 役牌 ＞ 客风牌**

役牌因为可以通过鸣牌直接确保 1 番，所以往往比幺九牌更重要。
但字牌的弱点也很明显：**场上只要切出 1 张，价值就会明显下降；如果 2 张都见了，基本就很难再指望它。**

所以，已经变弱的字牌很多时候只会作为防守时的安全牌留下。

## 2. 牌的相互作用

即使都是孤张数牌，彼此相隔 3 张的组合，通常也不理想。

尤其是 **1-4** 和 **6-9** 这两类组合，里面的 1 和 9 往往几乎没有实际价值。

<img src="../hai/pin1.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> → 受入是 <img src="../hai/pin1.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> ～ <img src="../hai/pin6.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，但去掉重叠部分后，几乎和只拿着 <img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 差不多。

<img src="../hai/pin6.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> → 受入是 <img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> ～ <img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，去掉重叠后，也和只拿着 <img src="../hai/pin6.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 相差不大。

像 `1-4` 这种组合里，1 真正能派上大用场，往往得摸进 `2-3-5-6` 这种能一下扩成两组搭子的牌形。
如果做不到，1 基本就是拖累。

这种相隔 3 张的持牌方式，日文里叫 `スジ`。在牌理上，你可以直接记成：

**如果孤张按筋持有，两张牌的受入会发生重叠，结果就是总受入变少。**

最典型的就是 1-4、6-9。
2-5、3-6、4-7、5-8 也同样会出现这种负面效果，只是没有那么极端。

<table border="1" cellpadding="4">
<tr>
<td width="60" bgcolor="#0000FF" class="white"><div align="center">手牌</div></td>
<td colspan="7" bgcolor="#0000FF" class="white"><div align="center">能组成搭子的摸牌</div></td>
</tr>
<tr>
<td width="60"><img src="../hai/man2.gif" width="24" height="34"></td>
<td><img src="../hai/man1.gif" width="24" height="34"></td>
<td bgcolor="#FF0000"><img src="../hai/man3.gif" width="24" height="34"></td>
<td bgcolor="#FF0000"><img src="../hai/man4.gif" width="24" height="34"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td width="60"><img src="../hai/man5.gif" width="24" height="34"></td>
<td></td>
<td bgcolor="#FF0000"><img src="../hai/man3.gif" width="24" height="34"></td>
<td bgcolor="#FF0000"><img src="../hai/man4.gif" width="24" height="34"></td>
<td><img src="../hai/man6.gif" width="24" height="34"></td>
<td><img src="../hai/man7.gif" width="24" height="34"></td>
<td></td>
<td></td>
</tr>
<tr>
<td width="60"><img src="../hai/man2.gif" width="24" height="34"><img src="../hai/man5.gif" width="24" height="34"></td>
<td><img src="../hai/man1.gif" width="24" height="34"></td>
<td><img src="../hai/man3.gif" width="24" height="34"></td>
<td><img src="../hai/man4.gif" width="24" height="34"></td>
<td><img src="../hai/man6.gif" width="24" height="34"></td>
<td><img src="../hai/man7.gif" width="24" height="34"></td>
<td></td>
<td></td>
</tr>
<tr>
<td width="60">（比较）<br /><img src="../hai/sou2.gif" width="24" height="34"><img src="../hai/man5.gif" width="24" height="34"></td>
<td><img src="../hai/sou1.gif" width="24" height="34"></td>
<td><img src="../hai/sou3.gif" width="24" height="34"></td>
<td><img src="../hai/sou4.gif" width="24" height="34"></td>
<td><img src="../hai/man3.gif" width="24" height="34"></td>
<td><img src="../hai/man4.gif" width="24" height="34"></td>
<td><img src="../hai/man6.gif" width="24" height="34"></td>
<td><img src="../hai/man7.gif" width="24" height="34"></td>
</tr>
</table>

看表就很清楚了。拿着 <img src="../hai/man2.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/man5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 时，<img src="../hai/man3.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 和 <img src="../hai/man4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 的受入重叠了，所以合并后的有效牌反而比想象中少。

以 2-5 为例，摸 1 只会形成边张，所以并不值得高兴。2-5 这种形状，真正的意义在于保留 2，等待摸 3 后形成两面。
也就是说：

1. 如果 1 已经很薄，2 的价值会继续下降。
2. 如果 5 是赤牌，2 的价值也会下降。

5-8 里的 8 也是同样的道理。

至于 3-6、4-7，因为两边的牌本身价值都比较高，序盘不用太在意“按筋持有”这件事。
但如果到了类似“靠黏连成一向听”的场面，按筋持有就会变成明显的不利因素。

**例**

<img src="../hai/man7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin1.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin2.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin3.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou8.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/haku.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/haku.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/haku.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 宝牌<img src="../hai/pin3.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />

这里如果切 <img src="../hai/man7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，其实是亏的。
因为同时保留 <img src="../hai/pin4.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 和 <img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，就把按筋持有的负面效果完整吃下来了。

如果没有其他额外条件，这道题的正解是切 <img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />。

### 理论 / 总结

按筋持有孤张，会让有效牌受入互相重叠，因此总受入减少。
尤其是 `1-4` 里的 1，和 `6-9` 里的 9，几乎很难再成为有效的面子候选，通常应该尽早处理。

最后再说一下相隔 4 张的组合，也就是：`1-5 / 2-6 / 3-7 / 4-8 / 5-9` 这 5 种。

过去有一种常见想法，认为这种牌形“只要摸到中间，就能形成两嵌张，所以应该重视”。

**例**

<img src="../hai/pin5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 自摸 <img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，看上去似乎形成了两嵌张

但这种想法其实没什么意义，甚至会有害。

因为就算没有 <img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，摸到 <img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 一样有受入。
比如把 <img src="../hai/pin5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 和 <img src="../hai/pin5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/sou9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 这类完全无关联的持牌相比，前者反而还少 1 种受入。

从 <img src="../hai/pin5.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 中先切掉 <img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" />，真正会后悔的情况，也只有后来刚好摸进 <img src="../hai/pin7.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /><img src="../hai/pin8.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 时而已。
这并不足以证明 <img src="../hai/pin9.gif" style="display:inline; vertical-align:middle; margin:0 1px; width:24px; height:34px;" /> 有什么特殊价值。

所以，相隔 4 张的组合即使有时能形成两嵌张，也不代表它本身就是优势牌形。结论很简单：**不要为了“将来可能渡成两嵌张”而高估这种组合。**
