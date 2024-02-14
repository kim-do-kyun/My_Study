# E/R Diagrams에서 관계 설계로의 변환
* DBMS를 이용한 구현
  * E/R 모델을 이용하여 설계 후 이를 관계모델로 변환
    * 각 엔티티 집합을 동일한 애트리뷰트 집합을 갖는 릴레이션으로 바꾼다
    * 관계성이 연결되어 있는 엔티티 집합들에 대한 키들을 애트리뷰트로 갖는 릴레이션으로 변환한다
  * 위와 같은 규칙으로 대부분 변환이 이루어지지만 특별한 경우도 있다
    * 약 엔티티 집합들은 릴레이션으로 직접 변환해서는 안된다
    * "isa" 관계성과 서브 클래스(subclass)들은 주의해서 다루어야 한다
    * 경우에 따라 두 릴레이션을 합치는 것이 좋다. 특히, 엔티티 집합 E에 대한 릴레이션과 E로부터 다대일(many-one) 관계성을 지니는 릴레이션을 합칠 수 있다

<br>

### 엔티티 집합을 릴레이션으로 변환
* 강엔티티 집합에 대하여 동일한 애트리뷰트들을 갖는 이름의 릴레이션을 생성

![스크린샷 2024-02-14 180326](https://github.com/kim-do-kyun/My_Study/assets/70315428/ef0c1751-20ce-420d-9333-919f20b4dd64)
* Movies(title, year, length, filmType), Stars(name, address), Studios(name, address)들로 릴레이션 생성

<br>

### E/R 관계성을 릴레이션으로 변환
* 관계성 R에 연관되는 각 엔티티 집합의 **키** 애트리뷰트들을 R에 대한 릴레이션 스키마의 애트리뷰트로 만든다
* 관계성이 애트리뷰트를 가지면 이 애트리뷰트도 릴레이션 R의 애트리뷰트로 만든다
* 위의 E/R다이어그램에서 Owns 변환시
  * Owns(title, year, studioName) (Movies의 키인 title, year, Studios의 키인 name로 구성)
  * Stars-in(title, year, starName)

<br>

### 릴레이션의 결합
* 다대일 관계성

![스크린샷 2024-02-14 180913](https://github.com/kim-do-kyun/My_Study/assets/70315428/719448bd-0004-430c-9e05-0fa7c946668f)

  * R에 대한 테이블을 생성하는 대신, S에 R의 모든 애트리뷰트들과 T의 키를 포함시켜도 된다
    * Owns, Movies릴레이션 결합

![스크린샷 2024-02-14 180956](https://github.com/kim-do-kyun/My_Study/assets/70315428/3733db8d-ab85-459b-9e2e-e32fd9e64777)

* 일대일 관계성

![스크린샷 2024-02-14 181046](https://github.com/kim-do-kyun/My_Study/assets/70315428/5f9a0cc7-0120-405f-bd6a-980a6e11e199)

  * R에 대한 테이블을 생성하는 대신, S에 R의 모든 애트리뷰트와 T의 키를 포함시켜도 된다(그 역도 가능)
* 다대일 관계성에서의 결합으로 만들어진 릴레이션과 다대다 관계성인 Stars-in으로부터 생성한 릴레이션 결합시 중복을 발생시킴(분할하여 중복성 제거해야함)

<br>

### 약 엔티티 집합의 변환
* 약 엔티티 집합 W에 대한 릴레이션은 W의 애트리뷰트들 뿐만 아니라 다대일 관계성에 의해서 W와 연관되어있는 W의 키를 형성하는데 도움을 주는 다른 키들도 포함해야 함
* W와 다른 엔티티 집합들을 연결시켜주는 다대일 관게성에 대해서는 릴레이션 생성x

![스크린샷 2024-02-14 181426](https://github.com/kim-do-kyun/My_Study/assets/70315428/f15deaa5-e7c5-4ece-a621-7da0b67fb2f9)
* Crews(number, studioName)으로 생성된다
* 만일 Unit-of를 릴레이션으로 만든다면 Unit-of(number, studioName, studioName')으로 생성되는데 여기서 studioName와 studioName'은 동일하므로 하나로 표현 가능
* 즉, Unit-of(number, studioName)으로 Crews의 릴레이션과 동일함