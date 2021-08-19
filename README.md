# _🎥 Movie Kiosk_ (Team Project)    
***
### Period : August 2021,  2weeks
### Personnel : 6 명.  
***
## 📌_Index_
* [Used Technology](#usedtechnology)
* [ER Diagram](#ER-Diagram)
***
## 📌 _Used Technology_       
## **JAVA 11 / Swing / Oracle**
***
### ER Diagram
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

</div>
</details>    
  

<details>
	<summary>ScrollPane Issue</summary>
	<div markdown="1"> 
	 <div> 장바구니 품목들은 각각 JPanel로 이루어져 있다.<br>   
그 패널 안에는 해당 품목의 이미지/이름/가격/수량이 들어가는데,<br>    
이 때 Panel의 Layout을 null로 지정해주어야 setBounds 함수로 원하는 위치에 삽입할 수 있다.<br>      
하지만 JScrollPane Component의 Layout을 Null로 지정하면 전체 장바구니의 스크롤기능이 들어가지를 않는다.<br>      
이 부분을 해결하기 위해서는, 각각의 품목 Panel의 요소들을 setBounds로 원하는 위치에 넣은 후에<br>      
그 JPanel을 다시 JPanel2에 넣어주고,JPanel2의 Layout을 Default값 BorderLayout으로 지정한다.<br>      
여기서 주위할점은 Scroll 기능은 양 사이드의 끝을 컴퓨터가 인지해야 들어가기 때문에<br>      
JScrollPane의 Component로 들어가는 JPanel안에 요소(JButton,JLabel)중 하나라도 "East","West"에 지정이 되있어야 한다<br>    </div>
	
	public Detail_P2_C(String img_path, String name, String price, String quantity, JFrame frame) {
	      LineBorder lineColor = new LineBorder(new Color(87,149,255));

	      setBackground(new Color(255, 255, 255));
	      setLayout(new BorderLayout());
	      setBorder(lineColor);
	      
	      ChkImg img = new ChkImg(img_path,94,87);
	      
	      add(img,"West");
	      
	      JPanel centerPanel = new JPanel();
	      centerPanel.setBackground(Color.white);
	      centerPanel.setLayout(null);
	      
	      JLabel proName = new JLabel(name);
	      proName.setFont(new Font("Lao MN", Font.BOLD | Font.ITALIC, 15));
	      proName.setForeground(Color.black);
	      proName.setBounds(20, 30, 200, 30);

	      JLabel proPrice = new JLabel(price + "원");
	      proPrice.setBounds(220, 30, 78, 31);
	      
	      JLabel proQuan = new JLabel(quantity + "개");
	      proQuan.setBounds(342, 35, 32, 16);
	      
	      JButton deleteBtn = new RoundedButton("Delete");
	      deleteBtn.setBounds(410, 30, 50, 50);
	      deleteBtn.setForeground(new Color(255, 0, 0));
	      deleteBtn.setBackground(new Color(255, 30, 255));
	      
	      centerPanel.add(proName);
	      centerPanel.add(proPrice);
	      centerPanel.add(proQuan);
	      centerPanel.add(deleteBtn);
	     
	      add(centerPanel,"Center");
	      
	      deleteBtn.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				new ProductsBasketsDAO().basketDelete(new ProductsBasket(proName.getText()));
				frame.setVisible(false);
				new DetailFrame();
			}
		});
	   }
----------------------------------------------------------------------------------------------------------------		
		
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
