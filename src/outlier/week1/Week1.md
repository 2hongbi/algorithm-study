# week 1 (21.09.05~21.09.18)
## 문제 상
### <선분 교차>
2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 알아보기
- 선 L1 : x1, y1, x2, y2
- 선 L2 : x3, y3, x4, y4
- 1,000,000 <= x1, x2, x3, x4, y1, y2, y3, y4 <= 1,000,000이며, 변수는 모두 정수
  
L1과 L2가 교차하면 1 <br>
L2와 L2가 교차하지 않으면 0
<br>
![선분교차1-문제](../../../img/cross_1.png)
![선분교차1-문제](../../../img/cross_2.png)

<hr>

### 문제 푸는 과정
<img src="https://latex.codecogs.com/svg.image?y=mx&plus;n" title="y=mx+n" />과 <img src="https://latex.codecogs.com/svg.image?y&space;=&space;m'&space;x&plus;&space;n'" title="y = m' x+ n'" /> 가 있다고 가정하자.
<br>
위 두 직선이 가질 수 있는 조건은 다음과 같다.
1. 만날 조건 : <img src="https://latex.codecogs.com/svg.image?m\neq&space;m'" title="m\neq m'" />
2. 평행 조건 : <img src="https://latex.codecogs.com/svg.image?m&space;=&space;m'" title="m = m'" />
3. 일치 조건 : <img src="https://latex.codecogs.com/svg.image?m=m',&space;n=n'" title="m=m', n=n'" />
4. 수직 조건 : <img src="https://latex.codecogs.com/svg.image?mm'=-1" title="mm'=-1" />

<br>

![선분교차1-문제푸는과정](../../../img/cross_3.jpg)

위의 조건들을 갖고 L1: (1, 5), (5, 1)과 L2: (1, 1), (5, 5)에 대입했다. <br>

L1는 <img src="https://latex.codecogs.com/svg.image?y&space;=&space;-x&plus;6&space;" title="y = -x+6 " />,
L2는 <img src="https://latex.codecogs.com/svg.image?y&space;=&space;x&space;" title="y = x " />로 위의 1번에 조건에 해당하여 만날 조건이 성사되었다.

<br>
하지만 두번째 가정에서 어긋났다. <br>
L1: (1, 1), (5, 5), L2: (6, 10), (10,6)을 지난다고 가정했을 때, 두 점을 지나는 직선이라고 가정한다면 위의 조건이 성립하지만, 선분이기 때문에 두 선분은 만나지 않았다. <br>

__*직선은 기울기가 다르기만 하면(평행하지 않을 때면) 교차하게 되는데, 선분이라 길이가 정해져 있는걸 간과했다.*__

<br>그래서 다른 방법을 고민했다.




<hr>

### 위 가정에서 확대해보기
만약, 둘 다 선분이라고 가정하지 말고, 하나의 직선과 하나의 선분으로 이루어졌다고 생각해보자. <br>
직선 하나가 다른 선분을 둘로 나누면 만난다고 생각할 수 있지 않을까? <br>

![선분교차1-문제푸는과정2](../../../img/cross_4.jpg)

즉, L1과 L2의 선분을 확장한 직선을 직선1, 직선2라고 가정하자. <br>
직선1에 의해 L2가 나누어진다면, 또 반대로 직선2에 의해 L1이 둘로 나누어진다면 둘은 만나다고 할 수 있지 않겠냐는 것이다. <br>
처음 가정에서 확대하여, 두 기울기가 서로 다르면, 즉 곱한 두 기울기가 0보다 작으면 직선 두개는 만난다고 볼 수 있겠다. <br>
*(f(x)=0라는 직선이 있다고 할 때, 두 점을 각각 넣어 기울기가 반대인 것을 확인하면 된다.)*

-> 직선을 기준으로 각각 반대 방향에 있으면 되지 않나?

![선분교차1-문제푸는과정](../../../img/cross_5.jpg)

<hr>

### 결과
![선분교차1-문제푸는과정](../../../img/cross_6.jpg)



