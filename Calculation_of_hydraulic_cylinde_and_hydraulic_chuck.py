'''
 * @file Calculation_of_hydraulic_cylinde_and_hydraulic_chuck.py
 * @date 27.05.2024
 * @author RMSHE
 *
 * < Calculation_of_hydraulic_cylinde_and_hydraulic_chuck.py >
 * Copyright(C) 2024 RMSHE. All rights reserved.
 *
 * This program is free software : you can redistribute it and /or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.If not, see < https://www.gnu.org/licenses/>.
 *
 * Electronic Mail : asdfghjkl851@outlook.com
'''

import numpy as np
import math


class MarkdownReport:
    report = ""

    def write_to_markdown_file(self, file_path):
        """
        向指定的Markdown文件写入内容。

        参数:
        file_path: 字符串,表示Markdown文件的路径。
        content: 字符串,按照Markdown格式准备的内容,将被写入文件。

        该函数将给定的内容写入指定路径的Markdown文件中,同时确保转义字符正确处理。
        """

        # 使用'with'语句打开或创建文件,保证即使发生错误文件也能正确关闭。
        # 'w'模式表示写入模式,如果文件已存在,其内容将被覆盖。
        # 指定编码为'utf-8'以支持多语言字符。
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.report)  # 将Markdown内容写入文件

    def generatingFormulas(self):
        return

    def export(self):
        self.report = self.report + f"""
# 液压缸设计报告

| 液压缸的径向几何参数计算结果 |                                            |      |
| ---------------------------- | :----------------------------------------: | :--: |
| 参数                         |                     值                     | 单位 |
| 杆径比                       |             {Structure.杆径比}             |      |
| 活塞计算直径                 |        {Structure.活塞计算直径*1e3}        | $mm$ |
| 活塞标准直径                 |        {Structure.活塞标准直径*1e3}        | $mm$ |
| 活塞杆计算直径               |       {Structure.活塞杆计算直径*1e3}       | $mm$ |
| 活塞杆标准直径               |       {Structure.活塞杆标准直径*1e3}       | $mm$ |
| 缸筒的最小壁厚               |       {Structure.缸筒的最小壁厚*1e3}       | $mm$ |
| 缸筒的标准壁厚               |      { Structure.缸筒的标准壁厚*1e3}       | $mm$ |
| 缸筒标准外径                 |        {Structure.缸筒标准外径*1e3}        | $mm$ |
| 端盖受力的总和               |      {Structure.端盖受力的总和*1e-3}       | $kN$ |
| 液压缸端盖螺钉连接处的厚度   | {Structure.液压缸端盖螺钉连接处的厚度*1e3} | $mm$ |

| 液压缸的纵向几何参数计算结果 |                                            |      |
| ---------------------------- | :----------------------------------------: | :--: |
| 参数                         |                     值                     | 单位 |
| 活塞杆的最大允许计算长度     |  {Structure.活塞杆的最大允许计算长度*1e3}  | $mm$ |
| 活塞宽度                     |          {Structure.活塞宽度*1e3}          | $mm$ |
| 活塞杆导向套滑动面的长度     | {Structure.活塞杆_导向套_滑动面的长度*1e3} | $mm$ |
| 活塞杆最小导向长度           |     {Structure.活塞杆最小导向长度*1e3}     | $mm$ |
| 活塞杆导向长度               |       {Structure.活塞杆导向长度*1e3}       | $mm$ |
| 隔套宽度                     |         { Structure.隔套宽度*1e3}          | $mm$ |
| 缸筒长度                     |          {Structure.缸筒长度*1e3}          | $mm$ |

| 液压缸的性能参数核算 |                                        |         |
| -------------------- | :------------------------------------: | :-----: |
| 参数                 |                   值                   |  单位   |
| 液压缸的压力         |        {Performance.压力*1e-6}         |  $MPa$  |
| 液压缸的流量         |           {Performance.流量}           | $m^3/s$ |
| 活塞运动速度         |       {Performance.活塞运动速度}       |  $m/s$  |
| 活塞的行程时间       |         {Performance.行程时间}         |   $s$   |
| 活塞杆伸出时的推力   | { Performance.活塞杆伸出时的推力*1e-3} |  $kN$   |
| 活塞杆缩回时的拉力   | {Performance.活塞杆缩回时的拉力*1e-3}  |  $kN$   |
| 液压缸所做的功       |   {Performance.液压缸所做的功*1e-3}    |  $kJ$   |
| 液压缸的功率         |    {Performance.液压缸的功率*1e-3}     |  $kW$   |

| 液压夹头的计算              |                                      |      |
| --------------------------- | ------------------------------------ | ---- |
| 参数                        | 值                                   | 单位 |
| V形夹块斜面与竖直方向的夹角 | {Collet.V形夹块斜面与竖直方向的夹角} | $°$  |
| 夹头体斜面与竖直方向的夹角  | {Collet.夹头体斜面与竖直方向的夹角}  | $°$  |
| 机械效率                    | {Collet.机械效率}                    |      |
| 安全系数                    | {Collet.安全系数}                    |      |
| 夹块与工件的摩擦因数        | {Collet.夹块与工件的摩擦因数}        |      |
| 每个夹块所需的夹紧力        | {Collet.夹紧力*1e-3}                 | $kN$ |
| 夹头体与夹块的摩擦角        | {Collet.夹头体与夹块的摩擦角}        | $°$  |
| 夹头液压缸所需要的压力      | {Collet.液压缸所需的压力*1e-3}       | $kN$ |

---

# 液压缸设计步骤
## 初始数据


| 表1 初始数据               |       |                                           |         |
| -------------------------- | :---: | :---------------------------------------: | :-----: |
| 参数名                     | 符号  |                    值                     |  单位   |
| 液压源的额定压力           | $P_N$ |      {InitData.液压源_额定压力*1e-6}      |  $MPa$  |
| 液压源的额定流量           |  $Q$  |        {InitData.液压源_额定流量}         | $m^3/s$ |
| 液压源的最大工作压力       |  $P$  |    {InitData.液压源_最大工作压力*1e-6}    |  $MPa$  |
| 试验机的额定动静最大试验力 |  $F$  | {InitData.试验机_额定动静最大试验力*1e-3} |  $KN$   |
| 作动器的额定位移           |  $S$  |      {InitData.作动器_额定位移*1e3}       |  $mm$   |

---

## 1. 确定液压系统参数

**液压缸类型选择**: 双活塞杆等行程等速液压缸

### 1.1 初选系统压力

根据**表1初始数据**展示的液压源额定压力，液压系统的工作压力确定为 {InitData.液压源_额定压力*1e-6} MPa

为了确定活塞杆径 $d$ 与活塞直径 $D$ 的关系，引入杆径比 $\phi = d/D$，其比值可按照 **表2 按工作压力选取杆径比 d/D** 进行选择。

| 表2 按工作压力选取杆径比 d/D |          |           |      |
| ---------------------------- | -------- | --------- | ---- |
| 工作压力（MPa）              | ≤5.0     | 5.0~7.0   | ≥7.0 |
| d/D                          | 0.5~0.55 | 0.62~0.70 | 0.7  |

基于液压系统的工作压力，我们选定的杆径比为: 
$$
\phi =\\frac{{d}}{{D}}= \\frac{{活塞杆直径}}{{活塞直径}} = {Structure.杆径比}
$$

### 1.2 初选回油腔压力（背压力）

考虑到采用的是“双活塞杆等行程等速液压缸”，我们得到以下关系式：

$$
液压缸回油腔压力 = 液压缸工作腔压力 = 液压系统的工作压力 = {InitData.液压源_额定压力*1e-6} MPa
$$
$$
速比 = \\frac{{v_2}}{{v_1}}=\\frac{{有杆腔进油时活塞运动速度}}{{无杆腔进油时活塞运动速度}} = 1
$$

---

## 2. 计算液压缸的径向几何参数

### 2.1 计算活塞的直径

活塞的直径可通过下式计算：
$$
D=\\sqrt{{\\frac{{4 \\cdot F}}{{\\pi \\cdot [p_1-p_2 \\cdot (1-\\phi^2)]}}}}
$$

|  变量  | 定义                       |                    值                     | 单位  |
| :----: | :------------------------- | :---------------------------------------: | :---: |
|  $D$   | 活塞直径                   |       {Structure.活塞计算直径}        | $m$  |
|  $F$   | 活塞杆所受到的有效外负载力 | {InitData.试验机_额定动静最大试验力} | $N$  |
| $p_1$  | 液压缸工作腔压力           |        {Structure.工作腔压力}        | $Pa$ |
| $p_2$  | 液压缸回油腔压力           |        {Structure.回油腔压力}        | $Pa$ |
| $\\phi$ | 杆径比                     |            {Structure.杆径比}             |       |

考虑到我们选用了双活塞杆等行程等速液压缸，因此无需根据速比要求选择活塞杆直径。依据杆径比，我们可以初步计算出活塞杆直径: 
$$
d_{{calculate}}=\\phi \\cdot D
$$

| 变量              | 定义             | 值                             | 单位 |
| ----------------- | ---------------- | ------------------------------ | ---- |
| $d_{{calculate}}$ | 活塞杆的计算直径 | {Structure.活塞杆计算直径} | $m$ |
| $D$               | 活塞标准直径     | {Structure.活塞标准直径}   | $m$ |
| $\phi$           | 杆径比           | {Structure.杆径比}             |      |

液压缸内径(活塞直径) $D$ 和活塞杆直径 $d$ 的计算结果应根据国家标准规定的液压缸相关标准进行圆整。常用的液压缸内径及活塞杆直径信息可参考 **表3 液压缸的基本参数系列**。

- 选定的活塞标准直径 $D$ 为: ${Structure.活塞标准直径*1e3} mm$
- 选定的活塞杆标准直径 $d$ 为: ${Structure.活塞杆标准直径*1e3} mm$

| 表3 液压缸的基本参数系列                 |                                                                                                                                                    |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 液压缸的公称压力系列(GB/T 7938-1978)/MPa | 0.63，1.0，1.6，2.5，4，6.3，10，16，25，31.5，40.0                                                                                                |
| 液压缸内径系列(GB/T 2348-1993)/mm        | 8，10，12，16，20，25，32，40，50，63，80，(90)，100，(110)，125，(140)，160，(180)，200，(220)，250，(280)，320，(360)，400，(450)，500           |
| 活塞杆直径系列(GB/T 2348-1993)/mm        | 4，5，6，8，10，12，14，16，18，20，22，25，28，32，36，40，45，50，56，63，70，80，90，100，110，125，140，160，180，200，220，250，280，320，360 |

---

### 2.2 计算缸筒壁厚

我们的液压缸缸筒采用铸造制造方法，选用的缸筒材料为45号钢，该材料在温度低于100°C时的许用应力为$[\sigma]={Structure.缸筒材料_许用应力*1e-6}MPa$. 采用铸造缸筒时，壁厚由铸造工艺决定，需按照厚壁圆筒的计算公式校核壁厚。当$\delta=0.08\sim0.3$时，可使用以下公式进行缸筒壁厚的校核:
$$
p_{{max}}=1.5 \\cdot P_N
$$
$$
\\delta_{{min}}=\\frac{{p_{{max}} \\cdot D}}{{2.3 \\cdot [\\sigma]-3 \\cdot p_{{max}}}}
$$
|      变量      | 定义                 |                  值                   | 单位  |
| :------------: | :------------------- | :-----------------------------------: | :---: |
|   $P_{{max}}$    | 缸筒内的最高工作压力 | {Structure.缸筒内的最高工作压力} | $Pa$ |
|      $D$       | 活塞标准直径         |     {Structure.活塞标准直径}      | $m$  |
|     $P_N$      | 液压源的额定压力     |   {InitData.液压源_额定压力}    | $Pa$ |
|   $[\sigma]$   | 缸筒材料的许用应力   |  {Structure.缸筒材料_许用应力}   | $Pa$ |
| $\delta_{{min}}$ | 缸筒的最小壁厚       |    {Structure.缸筒的最小壁厚}     | $m$  |

根据**表4 缸筒壁厚$\delta$**，对于活塞标准直径为 ${Structure.活塞标准直径*1e3}mm$ 的情况，将缸筒的最小壁厚$\delta_{{min}}$向上圆整为:
$$
缸筒的标准壁厚\delta = {Structure.缸筒的标准壁厚*1e3}mm
$$
此时我们可以得到缸筒标准外径为:
$$
d_1=D+2 \\cdot δ
$$

|      变量      | 定义                 |                  值                   | 单位  |
| :------------: | :------------------- | :-----------------------------------: | :---: |
|   $d_1$   | 缸筒的标准外径 | {Structure.缸筒标准外径} | $m$ |
|      $D$       | 活塞标准直径         |     {Structure.活塞标准直径}      | $m$  |
| $\delta$ | 缸筒的标准壁厚       | {Structure.缸筒的标准壁厚} | $m$  |

| 表4 缸筒壁厚$\delta$ |           |      |      |      |      |      |      |      |      |      |      |      |
| :------------------: | :-------: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|     产品系列代号     | $P_N/MPa$ |  63  |  70  |  80  | *90  | 100  | *110 | 125  | *140 | 150  | 160  | *180 |
|          A           |    16     |  10  |  10  |  11  |  12  | 13.5 |  15  | 13.5 |  14  |  15  |  17  | 19.5 |
|          B           |    16     |  10  |      |  11  |  12  | 13.5 |  15  | 13.5 |  14  |  15  |  17  | 19.5 |
|          C           |    16     | 6.5  |      | 7.5  |  9   | 10.5 | 11.5 | 13.5 |  14  |  15  |  17  | 19.5 |
|          D           |    16     | 6.5  |      | 7.5  |      | 10.5 |      | 13.5 |      |      |  17  |      |
|          E           |    25     | 7.5  |      |  10  |      | 12.5 |      | 12.5 |  15  |      | 17.5 |  20  |
|          E           |    35     |  10  |      |  10  |      | 12.5 |      | 17.5 |  20  |      | 22.5 |  25  |
|          F           |    16     |  7   |      |  8   |      |  8   | 8.5  | 9.5  |  11  |      |  12  |      |
|          F           |    25     |  7   |      |  9   |      |  11  |  12  |  13  |  15  |      |  17  |      |
|          F           |    32     | 9.5  |      |  12  |      |  15  |  16  | 17.5 |  21  |      |  25  |      |
|          G           |     4     |      |      |      |      |      |      |      |      |      |      |      |
|          G           |     5     |      |      |      |      |      |      |      |      |  5   |      |      |
|          G           |     7     |  3   |      |  3   |      |  3   |      |  5   |      |      |      |      |
|          G           |   10.5    |      |      |      |      |      |      |      |      |      |      |      |

> **表4 注:** 
>
> 1. 带星号”*”的液压缸标准内径为GB/2348一93规定非优先选用。
> 2. $P_n$ -- 液压缸的额定压力。

---

### 2.3 计算液压缸端盖螺钉连接处的厚度

在液压缸中，有活塞杆通过的缸盖叫端盖，无活塞杆通过的缸盖叫缸头或缸底。端盖、缸底与缸筒构成闭的压力容腔，它不仅要有足够的强度以承受液压力，而且必须具备一定的连接强度。端盖上有活塞杆导向孔（导向套的孔)及防尘圈、密封槽圈，还有连接螺钉孔，受力情况比较复杂，设计不好容易损坏端盖上有导向孔和螺钉孔，所以与缸底的计算方法不同。我们采用螺钉连接的法兰式端盖。端盖和法兰的常用计算公式如下：

1. 首先计算液压缸端盖的受力:

$$
P=0.785 \\cdot D^2 \\cdot p+0.785 \\cdot ({{d_1}}^2-D^2) \\cdot q
$$

端盖密封材料选用聚四氟乙烯，其屈服极限为:${Structure.端盖密封材料屈服极限*1e-6}MPa$

| 变量  | 定义                                   |                值                | 单位 |
| :---: | :------------------------------------- | :------------------------------: | :--: |
|  $P$  | 端盖受力的总和                         |    {Structure.端盖受力的总和}    | $N$  |
|  $D$  | 活塞标准直径                           |     {Structure.活塞标准直径}     | $m$  |
|  $p$  | 液压系统的工作压力                     |        {System.工作压力}         | $Pa$ |
| $d_1$ | 缸筒标准外径                           |     {Structure.缸筒标准外径}     | $m$  |
|  $q$  | 附加密封压力(一般取密封材料的屈服极限) | {Structure.端盖密封材料屈服极限} | $Pa$ |

2. 计算液压缸法兰式端盖的厚度:

$$
d_2=0.5 \\cdot (d_1-D)+D
$$


$$
h=\\sqrt{{\\frac{{3 \\cdot P \\cdot (D_0-d_2)}}{{\\pi \\cdot d_1 \\cdot [\\sigma]}}}}
$$
初步选定端盖法兰安装螺纹孔的间距为: ${Structure.缸筒标准外径*1e3}mm$

|    变量    | 定义                       |                   值                   | 单位 |
| :--------: | :------------------------- | :------------------------------------: | :--: |
|    $h$     | 液压缸端盖螺钉连接处的厚度 | {Structure.液压缸端盖螺钉连接处的厚度} | $m$  |
|    $P$     | 端盖受力的总和             |       {Structure.端盖受力的总和}       | $N$  |
|   $D_0$    | 端盖法兰安装螺纹孔的间距   |  {Structure.端盖法兰安装螺纹孔的间距}  | $m$  |
|   $d_1$    | 缸筒标准外径               |        {Structure.缸筒标准外径}        | $m$  |
|    $D$     | 活塞标准直径               |        {Structure.活塞标准直径}        | $m$  |
|   $d_1$    | 缸筒标准外径               |        {Structure.缸筒标准外径}        | $m$  |
| $[\sigma]$ | 缸筒材料的许用应力         |     {Structure.缸筒材料_许用应力}      | $Pa$ |

---

## 3. 计算液压缸的纵向几何参数

### 3.1 计算活塞杆的最大允许计算长度

液压缸的活塞行程 $S$ 在初步设计阶段主要根据实际工作需求确定。由于活塞杆的细长特性，必须对其进行纵向弯曲强度校核及液压缸的稳定性计算。因此，实际所需的工作行程可能不会等同于液压缸稳定性所能允许的最大行程。为了计算行程，应首先计算出活塞杆的最大允许计算长度。
$$
L=1.01 \\cdot d^2 \\cdot \\sqrt{{\\frac{{n}}{{9.8 \\cdot P \\cdot n_k}}}}
$$
液压缸的安装方式为一端自由、一端刚性固定时，根据《现代机械设计手册》得到，末端条件系数 $n = 2$
| 变量  | 定义                     |                  值                  | 单位 |
| :---: | :----------------------- | :----------------------------------: | :--: |
|  $L$  | 活塞杆的最大允许计算长度 | {Structure.活塞杆的最大允许计算长度} | $m$  |
|  $P$  | 活塞杆的纵向压缩负载     | {InitData.试验机_额定动静最大试验力} | $N$  |
|  $d$  | 活塞杆的标准直径         |      {Structure.活塞杆标准直径}      | $m$  |
|  $n$  | 液压缸安装的末端条件系数 | {Structure.液压缸安装的末端条件系数} |      |
| $n_k$ | 安全系数( $n_k > 6$ )    |       {Structure.安全系数n_k}        |      |

---

### 3.2 选择“活塞宽度”和“活塞杆导向套滑动面的长度”

- 活塞宽度通常取活塞标准直径的(0.5~1)倍。
- 活塞杆导向套滑动面的长度通常取活塞标准直径的(0.6~1)倍。

据此，我们可以得出：
$$
B=0.75 \\cdot D
$$

$$
A=0.75 \\cdot D
$$

| 变量 | 定义                     |                   值                   | 单位 |
| :--: | :----------------------- | :------------------------------------: | :--: |
| $B$  | 活塞宽度                 |          {Structure.活塞宽度}          | $m$  |
| $A$  | 活塞杆导向套滑动面的长度 | {Structure.活塞杆_导向套_滑动面的长度} | $m$  |
| $D$  | 活塞标准直径             |        {Structure.活塞标准直径}        | $m$  |

---

### 3.3 计算活塞杆最小导向长度

对于一般的液压缸，最小导向长度应满足以下条件:
$$
H_{{min}}=\\frac{{S}}{{20}}+\\frac{{D}}{{2}}
$$

|    变量     | 定义                 |                 值                 | 单位 |
| :---------: | :------------------- | :--------------------------------: | :--: |
| $H_{{min}}$ | 活塞杆最小导向长度   | {Structure.活塞杆最小导向长度} | $m$ |
|     $S$     | 液压缸的最大工作行程 |  {InitData.作动器_额定位移}   | $m$ |
|     $D$     | 活塞标准直径         |    {Structure.活塞标准直径}    | $m$ |

当活塞杆全部外伸时，从活塞支承面中点到导向套滑动面中点的距离称为最小导向长度 $H_{{min}}$。如果导向长度过小，将使液压缸的初始挠度（间隙引起的挠度）增大，影响液压缸的稳定性，因此设计时必须保证有一最小导向长度。

---

### 3.4 选择"活塞杆导向长度"

- 活塞杆导向长度通常取活塞标准直径的(0.6~1.5)倍。
- 同时，需要确保活塞杆的导向长度不小于最小导向长度, 即: $H<H_{{min}}$

据此，我们计算得出:
$$
H={Structure.活塞杆最小导向长度的系数} \\cdot D
$$
注：计算结果应向上圆整。

| 变量 | 定义           |                              值                              | 单位 |
| :--: | :------------- | :----------------------------------------------------------: | :--: |
| $H$  | 活塞杆导向长度 | ${Structure.活塞杆导向长度} > H_{{min}}={Structure.活塞杆最小导向长度}$ | $m$  |
| $D$  | 活塞标准直径   |                   {Structure.活塞标准直径}                   | $m$  |

---

### 3.5 计算隔套宽度

为了确保活塞杆的最小导向长度，过度增加活塞杆导向套滑动面的长度或活塞宽度并不合适。在导向套与活塞之间安装隔套 $K$ 是一种更佳的解决方案，隔套宽度 $C$ 由所需的最小导向长度决定，计算公式为：
$$
C=H-\\frac{{A+B}}{{2}}
$$
采用隔套不仅有助于确保最小导向长度的需求，也有利于提升导向套和活塞的通用性。

| 变量 | 定义                     |                   值                   | 单位 |
| :--: | :----------------------- | :------------------------------------: | :--: |
| $B$  | 活塞宽度                 |          {Structure.活塞宽度}          | $m$  |
| $A$  | 活塞杆导向套滑动面的长度 | {Structure.活塞杆_导向套_滑动面的长度} | $m$  |
| $H$  | 活塞杆导向长度           |       {Structure.活塞杆导向长度}       | $m$  |
| $C$  | 隔套宽度                 |          {Structure.隔套宽度}          | $m$  |

注：如果已经能够保证活塞杆的最小导向长度，则无需安装隔套。

---

### 3.6 计算液压缸的缸筒长度

缸简长度 $L_1$ 由最大工作行程长度加上各种结构需要来确定，即:
$$
L_1=S+B+H+M+C
$$

| 变量  | 定义           |             值             | 单位 |
| :---: | :------------- | :------------------------: | :--: |
| $L_1$ | 缸筒长度       |    {Structure.缸筒长度}    | $m$  |
|  $B$  | 活塞宽度       |    {Structure.活塞宽度}    | $m$  |
|  $M$  | 活塞杆密封长度 | {Structure.活塞杆密封长度} | $m$  |
|  $H$  | 活塞杆导向长度 | {Structure.活塞杆导向长度} | $m$  |
|  $C$  | 隔套宽度       |    {Structure.隔套宽度}    | $m$  |

注: 一般缸简的长度最好不超过内径的20倍。

---

## 4. 液压缸的性能参数核算

### 4.1 计算液压缸的压力

$$
A=\\pi \\cdot [(0.5 \\cdot D)^2-(0.5 \\cdot d)^2]
$$


$$
p=\\frac{{F}}{{A}}
$$

| 变量 | 定义                       |                  值                  | 单位  |
| :--: | :------------------------- | :----------------------------------: | :---: |
| $p$  | 压力                       |          {Performance.压力}          | $Pa$  |
| $F$  | 活塞杆所受到的有效外负载力 | {InitData.试验机_额定动静最大试验力} |  $N$  |
| $A$  | 活塞的有效工作面积         |   {Performance.活塞的有效工作面积}   | $m^2$ |
| $D$  | 活塞直径                   |       {Structure.活塞计算直径}       |  $m$  |
| $d$  | 活塞杆的标准直径           |      {Structure.活塞杆标准直径}      |  $m$  |

----

### 4.2 计算活塞运动速度

对于装有双活塞杆的液压缸，其活塞运动速度的计算公式为:
$$
v=\\frac{{4 \\cdot Q \\cdot \\eta_v}}{{\\pi \\cdot (D^2-d^2)}}
$$
注: 这一公式适用于有活塞杆的情况下计算活塞运动速度，并不适用于无活塞杆的情形。

|   变量   | 定义                     |                值                |  单位   |
| :------: | :----------------------- | :------------------------------: | :-----: |
|   $v$    | 活塞运动速度             |    {Performance.活塞运动速度}    |  $m/s$  |
|   $Q$    | 流量(液压源的额定流量)   |        {Performance.流量}        | $m^3/s$ |
| $\eta_v$ | 容积效率(一般取0.9~0.95) |      {Performance.容积效率}      |         |
|   $A$    | 活塞的有效工作面积       | {Performance.活塞的有效工作面积} |  $m^2$  |
|   $D$    | 活塞直径                 |     {Structure.活塞计算直径}     |   $m$   |
|   $d$    | 活塞杆的标准直径         |    {Structure.活塞杆标准直径}    |   $m$   |

---

### 4.3 计算活塞的行程时间

对于配备双活塞杆的液压缸，计算活塞完成全部行程所需时间的公式为:
$$
t=\\frac{{\\pi \\cdot (D^2-d^2) \\cdot S}}{{4 \\cdot Q}}
$$
注: 这一公式适用于有活塞杆的情况下计算活塞运动速度，并不适用于无活塞杆的情形。

|   变量   | 定义                       |                值                |  单位   |
| :------: | :------------------------- | :------------------------------: | :-----: |
|   $t$    | 行程时间                   |      {Performance.行程时间}      |   $s$   |
|   $Q$    | 流量(液压源的额定流量)     |        {Performance.流量}        | $m^3/s$ |
| $\eta_v$ | 容积效率(一般取0.9~0.95)   |      {Performance.容积效率}      |         |
|   $A$    | 活塞的有效工作面积         | {Performance.活塞的有效工作面积} |  $m^2$  |
|   $D$    | 活塞直径                   |     {Structure.活塞计算直径}     |   $m$   |
|   $d$    | 活塞杆的标准直径           |    {Structure.活塞杆标准直径}    |   $m$   |
|   $S$    | 活塞行程(作动器的额定位移) |      {Performance.活塞行程}      |   $m$   |

---

### 4.4 计算活塞杆伸出和缩回时的推力和拉力

活塞杆伸出时的推力公式为：
$$
P_1=\\frac{{\\pi}}{{4}}[D^2(p-p_0)+d^2p_0]\\eta_g
$$
活塞杆缩回时的拉力公式为：
$$
P_2=\\frac{{\\pi}}{{4}}[D^2(p-p_0)-d^2p_0]\\eta_g
$$

|   变量   | 定义                      |                值                | 单位 |
| :------: | :------------------------ | :------------------------------: | :--: |
|  $P_1$   | 活塞杆伸出时的推力        | {Performance.活塞杆伸出时的推力} | $N$  |
|  $P_2$   | 活塞杆缩回时的拉力        | {Performance.活塞杆缩回时的拉力} | $N$  |
|   $D$    | 活塞直径                  |     {Structure.活塞计算直径}     | $m$  |
|   $d$    | 活塞杆的标准直径          |    {Structure.活塞杆标准直径}    | $m$  |
| $\eta_g$ | 机械效率(一般取0.85-0.95) |      {Performance.机械效率}      |      |
|   $p$    | 液压系统的工作压力        |      {Structure.工作腔压力}      | $Pa$ |
|  $p_0$   | 液压缸回油腔压力          |      {Structure.回油腔压力}      | $Pa$ |

---

### 4.5 计算液压缸所做的功和功率

液压缸所做的功的计算公式为：
$$
W=P \\cdot S
$$
液压缸的功率计算公式为：
$$
N=P \\cdot v
$$

| 变量 | 定义                                   |                值                | 单位  |
| :--: | :------------------------------------- | :------------------------------: | :---: |
| $W$  | 液压缸所做的功                         |   {Performance.液压缸所做的功}   |  $J$  |
| $N$  | 液压缸的功率                           |    {Performance.液压缸的功率}    |  $W$  |
| $v$  | 活塞运动速度                           |    {Performance.活塞运动速度}    | $m/s$ |
| $P$  | 活塞杆伸出时的推力or活塞杆缩回时的拉力 | {Performance.活塞杆伸出时的推力} |  $N$  |
| $S$  | 活塞行程(作动器的额定位移)             |      {Performance.活塞行程}      |  $m$  |

---
# 液压夹头的计算

## 1. 计算液压夹头所需要的夹紧力

计算液压夹头每个夹块所需的夹紧力可用以下公式:

$$
F_G=\\frac{{F}}{{2 \\cdot \\mu}} \\cdot \\sin(\\alpha \\cdot \\frac{{\\pi}}{{180}}) \\cdot S
$$

**注解:**

1. **安全系数**的取值通常介于2到3之间，具体取决于系统的动态变化和摩擦因数的稳定性：
- 当动态变化较小、摩擦因数保持不变，以及系统中液压油波动较小时，可取较小的安全系数值。
   - 相反，若系统的动态变化较大、摩擦因数变化显著，且存在较大的压缩空气波动和显著的加速度（无论是直线还是旋转运动），则应取较大的安全系数值。

2. **夹块与工件之间的摩擦因数**的选择应基于夹块材料和试样材料的特性。

|   变量    | 定义                                                         |                  值                  | 单位 |
| :-------: | :----------------------------------------------------------- | :----------------------------------: | :--: |
|   $F_G$   | 每个夹块所需的夹紧力                                         |           {Collet.夹紧力}            | $N$  |
|    $F$    | 试验机额定动静最大试验力                                     | {InitData.试验机_额定动静最大试验力} | $N$  |
|   $\mu$   | 夹块与工件的摩擦因数                                         |    {Collet.夹块与工件的摩擦因数}     |      |
| $\\alpha$ | V形夹块斜面与竖直方向的夹角(摆角, 当设为90°时, 该爪为普通平爪) | {Collet.V形夹块斜面与竖直方向的夹角} | $°$  |
|    $S$    | 安全系数                                                     |          {Collet.安全系数}           |      |

## 2. 计算夹头液压缸所需要的压力

设夹紧动作为正行程。通过对夹块采用斜面模型进行受力分析，可以得到以下计算公式：
$$
\\varphi = \\abs{{\\arctan(\\frac{{\\tan (\\theta \\cdot \\frac{{\\pi}}{{180}})}}{{\\eta}})-\\theta}}
$$
$$
P=F_G \\cdot \\tan([\\theta+\\varphi] \\cdot \\frac{{\\pi}}{{180}})
$$

|    变量    | 定义                       |                 值                  | 单位 |
| :--------: | :------------------------- | :---------------------------------: | :--: |
|   $F_G$    | 每个夹块所需的夹紧力       |           {Collet.夹紧力}           | $N$  |
|    $P$     | 夹头液压缸所需要的压力     |      {Collet.液压缸所需的压力}      | $N$  |
|   $\eta$   | 机械效率(一般取0.85-0.95)  |          {Collet.机械效率}          |      |
| $\\theta$  | 夹头体斜面与竖直方向的夹角 | {Collet.夹头体斜面与竖直方向的夹角} | $°$  |
| $\\varphi$ | 夹头体与夹块的摩擦角       |    {Collet.夹头体与夹块的摩擦角}    | $°$  |

**注**: 在本章中，设计液压缸和计算液压夹头时使用的所有三角函数均应按弧度制进行计算。因此，必须先将角度制转换为弧度制。

---

        """

        self.write_to_markdown_file('液压缸设计报告.md')
        return


class TableHandler:
    def __init__(self, table):
        """
        :param self.table: 表格数据。
        """
        self.table = table
        pass

    def remove_trailing_zeros(self, number: float):
        """
        去除浮点数尾部多余的0。

        :param number: 需要处理的浮点数。
        :return: 去除尾部多余0后的字符串。
        """
        str_number = str(number)
        if '.' in str_number:
            str_number = str_number.rstrip('0').rstrip('.')
        return str_number

    def closest(self, target: str, mode="closest",):
        """
        在列表中查找与目标值最接近的数。

        :param target: 目标数值（字符串格式）。
        :param mode: 查找模式,包括"closest(最近)"、"up(向上)"、"down(向下)"。
        :return: 与目标值最接近的数（字符串格式）。
        """
        numbers = self.table
        if not numbers:
            return None
        target = float(target)
        numbers = [float(num) for num in numbers if num]
        filtered_numbers = {
            "up": [num for num in numbers if num > target],
            "down": [num for num in numbers if num < target]
        }.get(mode, numbers)

        if not filtered_numbers:
            return None

        closest = min(filtered_numbers, key=lambda num: abs(num - target))
        return self.remove_trailing_zeros(closest)

    def find(self, row_index: str = "", col_index: str = ""):
        """
        二维表格查表函数。
        如果两个索引都提供了,则返回对应的单元格数据
        当行索引或列索引为空字符串时返回行索引所再的整行数据或列索引所再的整列数据

        :param row_index: 行索引。
        :param col_index: 列索引。
        :return: 根据索引返回的数据。
        """
        table = self.table
        # 如果两个索引都未提供,返回None
        if row_index == "" and col_index == "":
            return None

        # 如果只提供了列索引,返回整列数据
        if row_index == "":
            col_pos = table[0].index(
                col_index) if col_index in table[0] else -1
            if col_pos != -1:
                return [row[col_pos] for row in table[1:]]  # 从第二行开始取值,忽略表头
            else:
                return None

        # 如果只提供了行索引,返回整行数据
        if col_index == "":
            for row in table:
                if row[0] == row_index:
                    return row[1:]  # 返回整行数据,不包括行头
            return None

        # 如果两个索引都提供了,找到对应的单元格数据
        row_pos = next((i for i, row in enumerate(
            table) if row[0] == row_index), None)
        if row_pos is not None and col_index in table[0]:
            col_pos = table[0].index(col_index)
            return table[row_pos][col_pos]
        return None

    def reverseFind(self, cell_value: str, index_value: str, search_type: str, index_number: str):
        """
        对表格进行反向查找的函数,返回所有匹配项的列表

        :param cell_value: 要查找的单元格的值
        :param index_value: 已知的行索引值或列索引值
        :param search_type: 搜索类型（"row":在行中搜索 或 "col":在列中搜索)
        :param index_number: 选择在表格的第几行或列查找
        :return: 匹配的行索引值或列索引值的列表
        """
        matches = []
        if search_type == "col":
            col_index = self.table[0].index(index_value)
            matches = [row[index_number]
                       for row in self.table if row[col_index] == cell_value]
        elif search_type == "row":
            row_index = next((i for i, row in enumerate(
                self.table) if row[0] == index_value), -1)
            if row_index != -1:
                matches = [self.table[index_number][i] for i, col_value in enumerate(
                    self.table[row_index]) if col_value == cell_value]
        return matches if matches else ["Not Found"]


class HydraulicStructureStructure:
    工作腔压力 = None  # Pa
    回油腔压力 = None  # Pa
    杆径比 = None  # 活塞杆直径/活塞直径
    缸筒材料_许用应力 = None  # Pa
    活塞计算直径 = None  # m
    活塞标准直径 = None  # m
    活塞杆计算直径 = None  # m
    活塞杆标准直径 = None  # m
    缸筒内的最高工作压力 = None  # Pa
    缸筒的最小壁厚 = None  # m
    缸筒的标准壁厚 = None  # m
    缸筒标准外径 = None  # m
    端盖密封材料屈服极限 = None  # Pa
    端盖受力的总和 = None  # N
    液压缸端盖螺钉连接处的厚度 = None  # m
    端盖法兰安装螺纹孔的间距 = None  # m

    活塞杆的最大允许计算长度 = None  # m
    液压缸安装的末端条件系数 = None
    安全系数n_k = None
    活塞杆最小导向长度 = None  # m
    活塞杆导向长度 = None  # m
    隔套宽度 = None  # m
    活塞杆_导向套_滑动面的长度 = None  # m
    活塞宽度 = None  # m
    活塞杆密封长度 = None  # m
    缸筒长度 = None  # m

    活塞杆最小导向长度的系数 = None

    def selection_of_rod_diameter_ratio(self):
        """
        按工作压力选取杆径比
        """
        if System.工作压力*1e-6 <= 5.0:  # Pa *-> MPa
            self.杆径比 = 0.525
        elif System.工作压力*1e-6 > 5.0 and System.工作压力*1e-6 < 7.0:  # Pa *-> MPa
            self.杆径比 = 0.66
        elif System.工作压力*1e-6 > 7.0:  # Pa *-> MPa
            self.杆径比 = 0.7

        return self.杆径比

    def pistonDiameter(self):
        """
        计算活塞直径

        :formulas: D=\sqrt{\frac{4 \cdot F}{\pi \cdot [p_1-p_2 \cdot (1-\phi^2)]}}
        :units: D -- 活塞直径 m
        :units: F -- 活塞杆所受到的有效外负载力 N
        :units: p1 -- 液压缸工作腔压力 Pa
        :units: p2 -- 液压缸回油腔压力 Pa
        :units: φ -- 杆径比
        """
        self.活塞计算直径 = np.sqrt(
            (4*InitData.试验机_额定动静最大试验力)/(np.pi*(self.工作腔压力-self.回油腔压力*(1-pow(self.杆径比, 2)))))

        return self.活塞计算直径

    def pistonRodDiameter(self):
        """
        计算活塞杆直径

        :formulas: \phi=d/D
        :units: D -- 活塞标准直径 m
        :units: d -- 活塞杆计算直径 N
        :units: φ -- 杆径比
        """
        self.活塞杆计算直径 = self.杆径比*self.活塞标准直径

        return self.活塞杆计算直径

    def cylinderWallThick(self):
        """
        计算铸造缸筒壁厚

        :formulas: p_{max}<=1.5 \cdot PN
        :formulas: \delta>=\frac{p_{max} \cdot D}{2.3 \cdot [\sigma]-3 \cdot p_{max}}
        :units: P_max -- 缸筒内的最高工作压力 Pa
        :units: D -- 活塞标准直径 m
        :units: PN -- 额定压力 Pa
        :units: [σ] -- 缸筒材料的许用应力 Pa
        :units: δ -- 缸筒的最小壁厚 m
        """
        self.缸筒内的最高工作压力 = 1.5*InitData.液压源_额定压力
        self.缸筒的最小壁厚 = (self.缸筒内的最高工作压力*self.活塞标准直径) / \
            (2.3*self.缸筒材料_许用应力-3*self.缸筒内的最高工作压力)

        return self.缸筒的最小壁厚

    def cylinderOutsideDiameter(self):
        """
        计算缸筒的标准外径

        :formulas: D1=D+2 \cdot δ
        :units: D1 -- 缸筒的标准外径 m
        :units: D -- 活塞标准直径 m
        :units: δ -- 缸筒的标准壁厚 m
        """
        self.缸筒标准外径 = round(self.活塞标准直径+2*self.缸筒的标准壁厚, 3)

        return self.缸筒标准外径

    def cylinderCapForce(self):
        """
        计算液压缸端盖的受力

        :formulas: P_1=0.785 \cdot d^2 \cdot p
        :formulas: P_2=0.785 \cdot ({d_1}^2-d^2) \cdot q
        :formulas: P=P1+P2
        :units: P1 -- 活塞杆伸出时的推力 N
        :units: P2 -- 活塞杆缩回时的拉力 N
        :units: P -- 端盖受力的总和 N
        :units: d -- 缸筒内径 = 活塞标准直径 m
        :units: d1 -- 缸筒标准外径 m
        :units: p -- 工作压力 Pa
        :units: q -- 附加密封压力(一般取密封材料的屈服极限) Pa
        """

        '''
        self.eta_g = 0.9  # 机械效率,一般取0.85-0.95

        # 活塞杆伸出时的推力(N)
        self.活塞杆伸出时的推力 = (np.pi/4)*(pow(self.活塞标准直径, 2)*(System.工作压力-self.回油腔压力) +
                                    pow(self.活塞杆标准直径, 2)*self.回油腔压力)*self.eta_g

        # 活塞杆缩回时的拉力(N)
        self.活塞杆缩回时的拉力 = (np.pi/4)*(pow(self.活塞标准直径, 2)*(System.工作压力-self.回油腔压力) -
                                    pow(self.活塞杆标准直径, 2)*self.回油腔压力)*self.eta_g

        # 端盖受力的总和(N)
        self.端盖受力的总和 = self.活塞杆伸出时的推力+self.活塞杆缩回时的拉力
        
        '''
        self.端盖受力的总和 = 0.785*pow(self.活塞标准直径, 2)*System.工作压力 + \
            0.785*(pow(self.缸筒标准外径, 2)-pow(self.活塞标准直径, 2))*self.端盖密封材料屈服极限

        return self.端盖受力的总和

    def cylinderCapThick(self):
        """
        计算液压缸法兰式端盖螺钉连接处的厚度

        :formulas: h=\sqrt{\frac{3 \cdot P \cdot (D_0-d_2)}{\pi \cdot d_1 \cdot [\sigma]}}
        :units: P -- 端盖受力的总和 N
        :units: h -- 液压缸端盖螺钉连接处的厚度 m
        :units: D0 -- 端盖法兰安装螺纹孔的间距 m
        :units: d2 -- 缸筒外径与缸筒内径的中值直径 m
        :units: d1 -- 缸筒标准外径 m
        :units: [σ] -- 缸筒材料的许用应力 Pa
        """

        # 计算缸筒外径与缸筒内径的中值直径(m)
        d_2 = (0.5*self.缸筒标准外径-0.5*self.活塞标准直径)+self.活塞标准直径

        # 计算端盖螺钉连接处的厚度(m)
        self.液压缸端盖螺钉连接处的厚度 = np.sqrt((3*self.端盖受力的总和*(self.端盖法兰安装螺纹孔的间距-d_2)) /
                                     (np.pi*self.缸筒标准外径*self.缸筒材料_许用应力))

        return self.液压缸端盖螺钉连接处的厚度

    def maximum_permissible_calculated_length_of_piston_rod(self):
        """
        计算活塞杆的最大允许计算长度

        :formulas: L=1.01 \cdot d^2 \cdot \sqrt{\frac{n}{9.8 \cdot P \cdot n_k}}
        :units: L -- 活塞杆的最大允许计算长度 m
        :units: P -- 活塞杆的纵向压缩负载 N
        :units: d -- 活塞杆的标准直径 m
        :units: n -- 液压缸安装的末端条件系数
        :units: n_k -- 安全系数 (n_k > 6)
        """
        self.活塞杆的最大允许计算长度 = 1.01 * \
            pow(self.活塞杆标准直径, 2) * \
            np.sqrt(self.液压缸安装的末端条件系数/9.8*InitData.试验机_额定动静最大试验力*self.安全系数n_k)

        return self.活塞杆的最大允许计算长度

    def minimum_guide_length_of_piston_rod(self):
        """
        计算活塞杆最小导向长度

        :formulas: H>=\frac{S}{20}+\frac{D}{2}
        :units: H -- 活塞杆最小导向长度 m
        :units: S -- 液压缸的最大工作行程 m
        :units: D -- 活塞的标准直径 m
        """
        self.活塞杆最小导向长度 = InitData.作动器_额定位移/20+self.活塞标准直径/2

        return self.活塞杆最小导向长度

    def selection_of_piston_rod_guide_length(self):
        """
        1. 选择活塞杆导向长度:一般取(0.6~1.5)*活塞标准直径

        2. 计算隔套宽度
        :formulas: C=H-\frac{A+B}{2}
        :units: H -- 活塞杆导向长度 m
        :units: C -- 隔套宽度 m
        :units: A -- 活塞杆导向套滑动面的长度 m
        :units: B -- 活塞宽度 m
        """
        k = 0.6
        while k < 1.5:
            if k*self.活塞标准直径 > self.活塞杆最小导向长度:
                break
            k += 0.001

        self.活塞杆最小导向长度的系数 = k

        self.活塞杆导向长度 = math.ceil(k*self.活塞标准直径*1e3)*1e-3  # m *-> mm, mm *-> m

        self.隔套宽度 = self.活塞杆导向长度-(self.活塞杆_导向套_滑动面的长度+self.活塞宽度)/2

        # 如果已经能够保证活塞杆最小导向长度则不需要安装隔套
        if self.隔套宽度 < 0:
            self.隔套宽度 = 0

        return self.活塞杆导向长度

    def cylinderLength(self):
        """
        计算缸筒长度

        :formulas: L_1=S+B+H+M+C
        :units: L1 -- 缸筒长度 m
        :units: S -- 活塞的最大工作行程 m
        :units: B -- 活塞宽度 m
        :units: H -- 活塞杆导向长度 m
        :units: M -- 活塞杆密封长度 m
        :units: C -- 隔套宽度 m
        """
        self.缸筒长度 = InitData.作动器_额定位移+self.活塞宽度+self.活塞杆导向长度+self.活塞杆密封长度+self.隔套宽度

        return self.缸筒长度


class HydraulicCylinderPerformance:
    压力 = None  # Pa
    活塞的有效工作面积 = None  # m^2
    流量 = None  # m^3/s
    活塞运动速度 = None  # m/s
    速比 = None  # 有杆腔进油时活塞运动速度/无杆腔进油时活塞运动速度
    行程时间 = None  # s
    活塞杆伸出时的推力 = None  # N
    活塞杆缩回时的拉力 = None  # N
    液压缸所做的功 = None  # J
    液压缸的功率 = None  # W
    容积效率 = None
    活塞行程 = None  # m
    机械效率 = None

    def pressures(self):
        """
        计算液压缸的压力

        :formulas: p=F/A
        :units: p -- 压力 Pa
        :units: F -- 活塞杆所受到的有效外负载力 N
        :units: A -- 活塞的有效工作面积 m^2
        """
        self.活塞的有效工作面积 = np.pi * \
            pow(0.5*Structure.活塞标准直径, 2)-np.pi*pow(0.5*Structure.活塞杆标准直径, 2)

        self.压力 = InitData.试验机_额定动静最大试验力/self.活塞的有效工作面积

        return self.压力

    def flowRate(self):
        """
        计算液压缸的流量(双杆活塞)->流量已知

        :formulas: Q=\frac{\pi}{4} \cdot (D^2-d^2) \cdot v
        :units: Q -- 流量 m^3/s
        :units: D -- 液压缸内径 = 活塞标准直径 m
        :units: d -- 活塞杆标准直径 m
        :units: v -- 活塞运动速度 m/s
        """
        self.流量 = InitData.液压源_额定流量

        return self.流量

    def movementSpeed(self):
        """
        计算液压缸的活塞运动速度

        :formulas: v=\frac{4 \cdot Q \cdot \eta_v}{\pi \cdot (D^2-d^2)}
        :units: v -- 活塞运动速度 m/s
        :units: Q -- 流量 m^3/s
        :units: A -- 活塞的有效工作面积 m^2
        :units: D -- 液压缸内径 = 活塞标准直径 m
        :units: d -- 活塞杆标准直径 m
        :units: η_v -- 容积效率, 一般取0.9~0.95
        """
        self.容积效率 = 0.925

        self.活塞运动速度 = (4*self.流量*self.容积效率) / \
            (np.pi*(pow(Structure.活塞标准直径, 2)-pow(Structure.活塞杆标准直径, 2)))

        return self.活塞运动速度

    def travelTime(self):
        """
        计算液压缸活塞在缸体内完成全部行程所需要的时间

        :formulas: t=\frac{\pi \cdot (D^2-d^2) \cdot S}{4 \cdot Q}
        :units: t -- 行程时间 s
        :units: Q -- 流量 m^3/s
        :units: A -- 活塞的有效工作面积 m^2
        :units: D -- 液压缸内径 = 活塞标准直径 m
        :units: d -- 活塞杆标准直径 m
        :units: S -- 活塞行程 m
        """
        self.活塞行程 = InitData.作动器_额定位移

        self.行程时间 = (np.pi*(pow(Structure.活塞标准直径, 2) -
                     pow(Structure.活塞杆标准直径, 2)) * self.活塞行程)/(4*self.流量)

        return self.行程时间

    def rodForce(self):
        """
        计算活塞杆伸出和缩回时的推力和拉力

        :formulas: P_1=\frac{\pi}{4}[D^2(p-p_0)+d^2p_0]\eta_g
        :formulas: P_2=\frac{\pi}{4}[D^2(p-p_0)-d^2p_0]\eta_g
        :units: P1 -- 活塞杆伸出时的推力 N
        :units: P2 -- 活塞杆缩回时的拉力 N
        :units: D -- 液压缸内径 = 活塞标准直径 m
        :units: d -- 活塞杆标准直径 m
        :units: p -- 工作压力 Pa
        :units: p0 -- 回油腔压力 Pa
        """

        self.机械效率 = 0.9  # 机械效率,一般取0.85-0.95

        # 活塞杆伸出时的推力(N)
        self.活塞杆伸出时的推力 = (np.pi/4)*(pow(Structure.活塞标准直径, 2)*(System.工作压力-Structure.回油腔压力) +
                                    pow(Structure.活塞杆标准直径, 2)*Structure.回油腔压力)*self.机械效率

        # 活塞杆缩回时的拉力(N)
        self.活塞杆缩回时的拉力 = (np.pi/4)*(pow(Structure.活塞标准直径, 2)*(System.工作压力-Structure.回油腔压力) -
                                    pow(Structure.活塞杆标准直径, 2)*Structure.回油腔压力)*self.机械效率

        return [self.活塞杆伸出时的推力, self.活塞杆缩回时的拉力]

    def WorkAndPower(self):
        """
        计算液压缸所做的功和功率

        :formulas: W=P \cdot S
        :formulas: N=P \cdot v
        :units: W -- 液压缸所做的功 J
        :units: N -- 液压缸的功率 W
        :units: P -- 活塞杆伸出时的推力or活塞杆缩回时的拉力 N
        :units: S -- 活塞行程 m
        :units: v -- 活塞运动速度 m/s
        """
        self.液压缸所做的功 = self.活塞杆伸出时的推力*self.活塞行程

        self.液压缸的功率 = self.活塞杆伸出时的推力*self.活塞运动速度

        return [self.液压缸所做的功, self.液压缸的功率]


class HydraulicCollet:
    夹紧力 = None  # N (每个夹块的夹紧力)
    V形夹块斜面与竖直方向的夹角 = None  # °,(当设为90°时, 该爪为普通平爪)
    夹块与工件的摩擦因数 = None
    安全系数 = None

    机械效率 = None  # (一般取0.85-0.95)
    液压缸所需的压力 = None  # N
    夹头体与夹块的摩擦角 = None  # °
    夹头体斜面与竖直方向的夹角 = None  # °

    def clampingForce(self):
        '''
        根据试验机额定动静最大试验力计算夹块所需的夹紧力

        :formulas: F_G=\frac{F}{2 \cdot \mu} \cdot \sin \alpha \cdot S
        :units: F_G -- 每个夹块所需的夹紧力 N
        :units: F -- 试验机额定动静最大试验力 N
        :units: \mu -- 夹块与工件的摩擦因数
        :units: \alpha -- V形夹块斜面与竖直方向的夹角(摆角) °
        :units: S -- 安全系数
        '''
        self.夹紧力 = (InitData.试验机_额定动静最大试验力/(2 * self.夹块与工件的摩擦因数)) * \
            np.sin(self.V形夹块斜面与竖直方向的夹角*(np.pi/180))*self.安全系数

        return self.夹紧力

    def pressure_required_for_collet_hydraulic_cylinders(self):
        '''
        计算夹头液压缸所需要的压力(夹紧时为正行程)

        :formulas: P=F_G \cdot \tan([\theta+\varphi] \cdot \frac{\pi}{180})
        :formulas: \varphi = \abs{\arctan(\frac{\tan \theta \cdot \frac{\pi}{180}}{\eta})-\theta}
        :units: F_G -- 每个夹块所需的夹紧力 N
        :units: P -- 夹头液压缸所需要的压力 N
        :units: \eta -- 机械效率(一般取0.85-0.95)
        :units: \theta -- 夹头体斜面与竖直方向的夹角 °
        :units: \varphi -- 夹头体与夹块的摩擦角 °
        '''
        self.夹头体与夹块的摩擦角 = np.abs(np.arctan(
            np.tan(self.夹头体斜面与竖直方向的夹角*(np.pi/180))/self.机械效率)-self.夹头体斜面与竖直方向的夹角)  # °

        self.液压缸所需的压力 = self.夹紧力 * \
            np.tan(self.夹头体斜面与竖直方向的夹角*(np.pi/180)+self.夹头体与夹块的摩擦角*(np.pi/180))

        return self.液压缸所需的压力


class HydraulicSystem:
    工作压力 = None  # Pa


class DataTable:
    # 液压缸的公称压力系列(MPa)
    液压缸的公称压力系列 = ["0.63", "1.0", "1.6", "2.5", "4",
                  "6.3", "10", "16", "25", "31.5", "40.0"]
    # 液压缸内径系列(mm)
    液压缸内径系列 = ['8', '10', '12', '16', '20', '25', '32', '40', '50', '63', '80', '90', '100', '110',
               '125', '140', '160', '180', '200', '220', '250', '280', '320', '360', '400', '450', '500']
    # 活塞杆直径系列(mm)
    活塞杆直径系列 = ['4', '5', '6', '8', '10', '12', '14', '16', '18', '20', '22', '25', '28', '32', '36', '40', '45', '50',
               '56', '63', '70', '80', '90', '100', '110', '125', '140', '160', '180', '200', '220', '250', '280', '320', '360']
    # 常用活塞杆直径(mm)(按速比查找)
    活塞杆直径d_D40to110 = [
        ["", "40", "50", "63", "80", "90", "100", "110"],
        ["1.46", "22", "28", "35", "45", "50", "55", "63"],
        ["3", "", "", "45", "50", "60", "70", "80"],
    ]
    活塞杆直径d_D125to250 = [
        ["", "125", "140", "160", "180", "200", "220", "250"],
        ["1.46", "70", "80", "90", "100", "110", "125", "140"],
        ["2", "90", "100", "110", "125", "140", "", ""],
    ]
    # 标准缸筒壁厚(mm)
    标准缸筒壁厚系列 = [
        ["Series", "PN", "40", "50", "63", "70", "80", "90", "100", "110", "125",
            "140", "150", "160", "180", "200", "220", "250", "280", "320", "360"],
        ["A", "16", "10", "10", "10", "10", "11", "12", "13.5", "15", "13.5", "14",
            "15", "17", "19.5", "22.5", "30", "31", "32", "30", ""],
        ["B", "16", "8.5", "9", "10", "", "11", "12", "13.5", "15", "13.5", "14",
         "15", "17", "19.5", "22.5", "26.5", "24.5", "", "28.5", ""],
        ["C", "16", "7", "6.75", "6.5", "", "7.5", "9", "10.5", "11.5", "13.5", "14",
         "15", "17", "19.5", "22.5", "26.5", "24.5", "22.5", "28.5", ""],
        ["D", "16", "5", "6.5", "6.5", "", "7.5", "", "10.5", "", "13.5", "",
         "", "17", "", "22.5", "26.5", "24.5", "35.5", "28.5", "37.5"],
        ["E", "25", "5", "5", "7.5", "", "10", "", "12.5", "", "12.5", "15",
         "", "17.5", "20", "22.5", "25", "25", "22", "30.5", ""],
        ["E", "35", "7.5", "7.5", "10", "", "10", "", "12.5", "", "17.5", "20",
         "", "22.5", "25", "27.5", "25", "37", "44", "43", ""],
        ["F", "16", "", "5.5", "7", "", "8", "", "8", "8.5", "9.5", "11",
         "", "12", "", "14", "", "18", "", "", ""],
        ["F", "25", "", "6", "7", "", "9", "", "11", "12", "13", "15",
         "", "17", "", "21", "", "26", "", "", ""],
        ["F", "32", "", "8", "9.5", "", "12", "", "15", "16", "17.5", "21",
         "", "25", "", "30", "", "35", "", "", ""],
        ["G", "4", "", "", "", "", "", "", "", "", "", "",
         "", "", "", "7.5", "", "", "", "", ""],
        ["G", "5", "", "", "", "", "", "", "", "", "", "",
         "5", "", "", "", "", "", "", "", ""],
        ["G", "7", "", "", "3", "", "3", "", "3", "", "5", "",
         "", "", "", "", "", "", "", "", ""],
        ["G", "10.5", "3", "3", "", "", "", "", "", "", "", "",
         "", "", "", "", "", "", "", "", ""],
    ]


class InitData:
    液压源_额定压力 = 21 * 1e6  # MPa *-> Pa
    液压源_额定流量 = 100 * 0.00001667  # L/min *-> m^3/s
    液压源_最大工作压力 = 25 * 1e6  # MPa *-> Pa
    试验机_额定动静最大试验力 = 100 * 1e3  # KN *-> N
    作动器_额定位移 = 50 * 1e-3  # mm *-> m


Th = TableHandler("")
System = HydraulicSystem()
Structure = HydraulicStructureStructure()
Performance = HydraulicCylinderPerformance()
Collet = HydraulicCollet()
report = MarkdownReport()


def 打印初始数据():
    print("\n--------初始数据-------")
    print("液压源的额定压力 =", InitData.液压源_额定压力*1e-6, "MPa")  # Pa *-> MPa
    print("液压源的额定流量 =", InitData.液压源_额定流量, "m^3/s")  # m^3/s
    print("液压源的最大工作压力 =", InitData.液压源_最大工作压力*1e-6, "MPa")  # Pa *-> MPa
    print("试验机的额定动静最大试验力 =", InitData.试验机_额定动静最大试验力*1e-3, "KN")  # N *-> KN
    print("作动器的额定位移 =", InitData.作动器_额定位移*1e3, "mm")  # m *-> mm


def 计算液压缸的径向几何参数():
    print("\n--------计算液压缸的径向几何参数--------")
    '''
    液压缸的类型的选择: 双活塞杆_等行程等速液压缸

    1. 确定液压系统参数
    1.1 初选系统压力, 并且按照工作压力选择杆径比
    '''
    System.工作压力 = InitData.液压源_额定压力  # Pa
    Structure.selection_of_rod_diameter_ratio()
    print("杆径比 =", Structure.杆径比)

    '''
    1.2 计算液压缸尺寸或液压马达排量
        初选回油腔压力(背压力), 由于选用"双活塞杆_等行程等速液压缸"因此有:
    '''
    Structure.回油腔压力 = Structure.工作腔压力 = System.工作压力  # Pa
    Performance.速比 = 1

    '''
    2. 计算液压缸的径向几何参数
    2.1 计算活塞直径, 查找活塞标准直径
    '''
    Structure.pistonDiameter()
    print("活塞计算直径 =", Structure.活塞计算直径*1e3, "mm")  # m *-> mm

    液压缸内径系列 = TableHandler(DataTable.液压缸内径系列)  # mm
    Structure.活塞标准直径 = int(液压缸内径系列.closest(
        Structure.活塞计算直径*1e3, "up"))*1e-3  # m *-> mm, mm *-> m
    print("活塞标准直径 =", Structure.活塞标准直径*1e3, "mm")  # m *-> mm

    '''
    2.1 计算活塞杆直径, 查找活塞杆标准直径
    '''
    Structure.pistonRodDiameter()
    print("活塞杆计算直径 =", Structure.活塞杆计算直径*1e3, "mm")  # m *-> mm

    活塞杆直径系列 = TableHandler(DataTable.活塞杆直径系列)  # mm
    Structure.活塞杆标准直径 = int(活塞杆直径系列.closest(
        Structure.活塞杆计算直径*1e3))*1e-3  # m *-> mm, mm *-> m
    print("活塞杆标准直径 =", Structure.活塞杆标准直径*1e3, "mm")  # m *-> mm

    '''
    2.2 计算缸筒壁厚, 使用铸造缸筒
        缸筒材料的选择, 缸筒材料选用: 
    '''
    Structure.缸筒材料_许用应力 = 140 * 1e6  # MPa *-> Pa

    Structure.cylinderWallThick()
    print("缸筒的最小壁厚 =", Structure.缸筒的最小壁厚*1e3, "mm")  # m *-> mm

    table1 = TableHandler(DataTable.标准缸筒壁厚系列)
    col_index = Th.remove_trailing_zeros(
        float(Structure.活塞标准直径*1e3))  # mm *-> m
    标准缸筒壁厚列表 = table1.find("", col_index)
    print("标准缸筒壁厚列表 =", 标准缸筒壁厚列表, "mm")

    table3 = TableHandler(标准缸筒壁厚列表)
    Structure.缸筒的标准壁厚 = eval(table3.closest(
        Structure.缸筒的最小壁厚*1e3, "up"))*1e-3  # m *-> mm, mm *-> m
    print("缸筒的标准壁厚 =", Structure.缸筒的标准壁厚*1e3, "mm")  # m *-> mm

    Structure.cylinderOutsideDiameter()
    print("缸筒标准外径 =", Structure.缸筒标准外径*1e3, "mm")  # m *-> mm

    '''
    2.3. 计算液压缸端盖螺钉连接处的厚度
        采用螺钉连接法兰式端盖, 端盖密封材料选择: 聚四氟乙烯, 屈服极限:23MPa
    1. 计算液压缸端盖的受力
    2. 计算液压缸法兰式端盖的厚度
    '''
    Structure.端盖密封材料屈服极限 = 23*1e6  # MPa *-> Pa
    Structure.cylinderCapForce()
    print("端盖受力的总和 =", Structure.端盖受力的总和*1e-3, "KN")  # N *-> KN

    Structure.端盖法兰安装螺纹孔的间距 = Structure.缸筒标准外径
    Structure.cylinderCapThick()
    print("液压缸端盖螺钉连接处的厚度 =", Structure.液压缸端盖螺钉连接处的厚度*1e3, "mm")  # m *-> mm


def 计算液压缸的纵向几何参数():
    '''
    3. 计算液压缸的纵向结构尺寸
    3.1 计算活塞杆的最大允许计算长度
        液压缸采用的安装方式为: 一端自由,一端刚性固定 => 液压缸安装的末端条件系数 = 2
    3.2 选择"活塞宽度:一般为(0.5~1)*活塞标准直径"和"活塞杆导向套滑动面的长度:一般为(0.6~1)*活塞标准直径"
    3.3 计算活塞杆最小导向长度
    3.4 选择"活塞杆导向长度:一般取(0.6~1.5)*活塞标准直径"
    3.5 计算隔套宽度(如果已经能够保证活塞杆最小导向长度则不需要安装隔套)
    3.6 计算缸筒长度
    '''
    Structure.液压缸安装的末端条件系数 = 2
    Structure.安全系数n_k = 7  # 安全系数n_k > 6 即可
    Structure.maximum_permissible_calculated_length_of_piston_rod()
    print("活塞杆的最大允许计算长度 =", Structure.活塞杆的最大允许计算长度*1e3, "mm")  # m *-> mm

    Structure.活塞宽度 = round(0.75*Structure.活塞标准直径*1e3) * \
        1e-3  # m *-> mm, mm *-> m
    Structure.活塞杆_导向套_滑动面的长度 = round(
        0.75*Structure.活塞标准直径*1e3)*1e-3  # m *-> mm, mm *-> m
    print("活塞宽度 =", Structure.活塞宽度*1e3, "mm")  # m *-> mm
    print("活塞杆导向套滑动面的长度 =", Structure.活塞杆_导向套_滑动面的长度*1e3, "mm")  # m *-> mm

    Structure.minimum_guide_length_of_piston_rod()
    print("活塞杆最小导向长度 =", Structure.活塞杆最小导向长度*1e3, "mm")  # m *-> mm

    Structure.selection_of_piston_rod_guide_length()
    print("活塞杆导向长度 =", Structure.活塞杆导向长度*1e3, "mm")  # m *-> mm
    print("隔套宽度 =", Structure.隔套宽度*1e3, "mm")  # m *-> mm

    Structure.活塞杆密封长度 = 2*1e-3  # mm *-> m
    Structure.cylinderLength()
    print("缸筒长度 =", Structure.缸筒长度*1e3, "mm")  # m *-> mm
    if Structure.缸筒长度 > 20*Structure.活塞标准直径:
        print("[警告] 缸筒长度超过内径的20倍.")


def 液压缸的性能参数核算():
    print("\n--------液压缸的性能参数核算-------")
    '''
    4. 计算液压缸的性能
    4.1 计算液压缸的压力
    4.2 计算活塞运动速度
    4.3 计算活塞的行程时间
    4.4 计算活塞杆伸出和缩回时的推力和拉力
    4.5 计算液压缸所做的功和功率
    '''
    Performance.pressures()
    print("液压缸的压力 =", Performance.压力*1e-6, "MPa")  # Pa *-> MPa

    Performance.flowRate()
    print("液压缸的流量 =", Performance.流量, "m^3/s")  # m^3/s

    Performance.movementSpeed()
    print("活塞运动速度 =", Performance.活塞运动速度, "m/s")  # m/s

    Performance.travelTime()
    print("活塞的行程时间 =", Performance.行程时间, "s")  # s

    Performance.rodForce()
    print("活塞杆伸出时的推力 =", Performance.活塞杆伸出时的推力*1e-3, "KN")  # N *-> KN
    print("活塞杆缩回时的拉力 =", Performance.活塞杆缩回时的拉力*1e-3, "KN")  # N *-> KN

    Performance.WorkAndPower()
    print("液压缸所做的功 =", Performance.液压缸所做的功*1e-3, "KJ")  # J *-> KJ
    print("液压缸的功率 =", Performance.液压缸的功率*1e-3, "KW")  # W *-> KW


def 液压夹头的计算():
    print("\n--------液压夹头的计算-------")
    '''
    1. 计算液压夹头所需要的夹紧力
        1.1 安全系数的取值一般在(2~3)之间.
            取较小值: 低的动态变化, 摩擦因数无变化, 系统中液压油没有波动
            取较大值: 高的动态变化, 摩擦因数变化相当大, 压缩空气的波动相当大, 加速度叠加很大（直线/旋转）
        1.2 夹块与工件的摩擦因数的取值要根据夹块材料和试样材料选择
    2. 计算夹头液压缸所需要的压力
    '''
    Collet.V形夹块斜面与竖直方向的夹角 = 66  # °, (当设为90°时, 该爪为普通平爪)
    Collet.安全系数 = 3
    Collet.夹块与工件的摩擦因数 = 0.25
    Collet.clampingForce()
    print("每个夹块所需的夹紧力 =", Collet.夹紧力*1e-3, "KN")  # N *-> KN

    Collet.机械效率 = 0.9
    Collet.夹头体斜面与竖直方向的夹角 = 12  # °
    Collet.pressure_required_for_collet_hydraulic_cylinders()
    print("夹头体与夹块的摩擦角 =", Collet.夹头体与夹块的摩擦角, "°")
    print("夹头液压缸所需要的压力 =", Collet.液压缸所需的压力*1e-3, "KN")  # N *-> KN


打印初始数据()
计算液压缸的径向几何参数()
计算液压缸的纵向几何参数()
液压缸的性能参数核算()
液压夹头的计算()


report.export()
