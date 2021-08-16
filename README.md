__# 🎥 Movie Kiosk (Team Project)    
***
### Period : August 2021,  2weeks
### Personnel : 6 명.  
***
## 📌 _Used Technology_       
## **JAVA 11 / Swing / Oracle**
***
### ERD
![Alt text](/path/to/img.jpg) erd사진 이미지파일에 넣고 불러오기 (사이즈 조절은 html문법으로 가능하다)   
<img src="/path/to/img.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>
***   
### Diagram  
   
   

   
*** 
## 📌 _Core Functions_
> __CRUD__
> > **CRUD기능 설명**
 
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("핵심 기능 코드");
  }
}
```
***
## 📌 _Core Trouble shooting_   
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("핵심 트러블 오류 해결 전 코드");
  }
}
```
> __해결 방법__
> > 해결방법 설명

```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("핵심 트러블 오류 해결 후 코드");
  }
}
```
## 📝  _Trouble_   
<details>
<summary>김의성 이슈 코드 작성</summary>
<div markdown="1">

이슈 해결과정 작성 


</div>
</details> 

<details>
<summary>윤수영 이슈 코드 작성</summary>
<div markdown="1">

이슈 해결과정 작성 


</div>
</details>    
   
```java
<details>
	<summary>ScrollPane Issue</summary>
	<div markdown="1"> 
		
		
		if(pbDAO.basketList().size() == 0) {
			JPanel noData = new JPanel();
			noData.setBackground(new Color(255,254,230));
			JLabel msg = new JLabel("장바구니에 상품이 없습니다");
			msg.setFont(new Font("Lucida Grande", Font.BOLD, 20));
			noData.add(msg);
			scroll = new JScrollPane(noData);
			add(scroll);
			scroll.setBounds(0, 67, 600, 383);
			scroll.setVisible(true);
		} else {
			
			for(int i = 0; i < pbDAO.basketList().size(); ++i) {
				
				panel2_1.add(new Detail_P2_C(
						pbDAO.basketList().get(i).getImgPath(),
						pbDAO.basketList().get(i).getName(),
						pbDAO.basketList().get(i).getPrice(),
						pbDAO.basketList().get(i).getQuantity(),
						this));
				
				panel2.add(panel2_1.get(i));
				
				prices.add(Integer.parseInt(pbDAO.basketList().get(i).getPrice()));
			}
			scroll = new JScrollPane(panel2);
			add(scroll);
			
			scroll.setBounds(0, 67, 600, 383);
			scroll.setVisible(true);
		}
								     
</div>							     
</details>
```
	
<details>
<summary>신은철 이슈 코드 작성</summary>
<div markdown="1">

이슈 해결과정 작성 


</div>
</details>    
<details>
<summary>이한나 이슈 코드 작성</summary>
<div markdown="1">

이슈 해결과정 작성 


</div>
</details>   
<details>
<summary>나지수 이슈 코드 작성</summary>
<div markdown="1">

이슈 해결과정 작성 


</div>
</details>  

***  

## 🔆 _Bragging Code_    

> `영화관 좌석표`
> > 간단설명   
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("자랑하고 싶은 코드");
  }
}
```   
> `동영상 삽입`
> > 간단설명   
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("자랑하고 싶은 코드");
  }
}
```   
***   

## 📸 _ScreenShot_   
<details>
<summary>GUI 화면 다 넣기</summary>
<div markdown="1">

핵심 이미지 불러오기  


</div>
</details>   


## _회고록_
~~~~~~~~~~작성~~~~~~~~~~~

_
_
