# _🎥 Movie Kiosk_ (Team Project)    
***
### Period : August 2021,  2weeks
### Personnel : 6 명.  
***
## 📌 _Environment_       
> UI
> > Java Swing

> Programming Language
> > Java version 11.0.1

> DataBase
> > Oracle DB version 18c
> > > 외부 라이브러리
> > > > ojdbc6.jar/HikariCP.jar/sql.jar
***
### 📌 _ER Diagram_
![erd](https://user-images.githubusercontent.com/84116965/129391140-79714a8c-9b84-44e0-84d0-d9c5f5ad916e.png)
***   
### 📌 _Usecase Diagram_  
   
   ![usecase](https://user-images.githubusercontent.com/84116965/129388756-5ee5683e-bd54-4be5-958f-33405dd59fb1.png)

   
*** 
## 📌 _Important_

- 디자인 패턴

  - MVC 패턴을 기반으로한 패키지 구성

![mvc](https://user-images.githubusercontent.com/84116965/129394319-e93b844f-7ddc-4608-b708-b31ccc3b31bb.png)

- Java Swing에 영상 출력

  - mp4파일을 gif로 변환 후 화면에 출력(https://ezgif.com/video-to-gif)



- Swing의 Timer 클래스를 이용한 동적인 처리

  - 해당 시간이 지난 후 이벤트 발생
***
## 📌 _Core Trouble shooting_   
```java
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
```
> __ScrollPane Issue__
> > 장바구니 품목들은 각각 JPanel로 이루어져 있다.<br>   
그 패널 안에는 해당 품목의 이미지/이름/가격/수량이 들어가는데,<br>    
이 때 Panel의 Layout을 null로 지정해주어야 setBounds 함수로 원하는 위치에 삽입할 수 있다.<br>      
하지만 JScrollPane Component의 Layout을 Null로 지정하면 전체 장바구니의 스크롤기능이 들어가지를 않는다.<br>      
이 부분을 해결하기 위해서는, 각각의 품목 Panel의 요소들을 setBounds로 원하는 위치에 넣은 후에<br>      
그 JPanel을 다시 JPanel2에 넣어주고,JPanel2의 Layout을 Default값 BorderLayout으로 지정한다.<br>      
여기서 주위할점은 Scroll 기능은 양 사이드의 끝을 컴퓨터가 인지해야 들어가기 때문에<br>      
JScrollPane의 Component로 들어가는 JPanel안에 요소(JButton,JLabel)중 하나라도 "East","West"에 지정이 되있어야 한다<br>

```java
public class ProductList {
  public static void main(String[] args) {
  	
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
  }
}
```
## 📝  _Troubles_   
<details>
	<summary>Cancel Seats & Rollback Button</summary>      
	
> Problem
> > 좌석을 고르는 과정에서 좌석을 선택한 후 마음이 바뀌어서 골랐던 것을 취소하기 위해 <br>한 번 더 클릭하면 원래의 색으로 돌아와야 했으나 버튼의 색깔을 받아오는 메서드를 찾지 못해 막혔었습니다.
> > > Solution 
> > > >각 버튼이 현재 선택이 되었는지 안되었는지 담아둘 배열을 전역변수로 만들어 두어 상태를 확인할 수 있다면 될 것이라고 생각했습니다<br> 클래스에 boolean 타입의 배열을 만든뒤 false상태에서 클릭을 했을 경우 해당 index의 값을 true로 바꿔주고 색깔을 바꿔주었으며<br> true에서 다시 클릭을 했을 경우 false로 바꾼 뒤 원래의 색깔로 나오게 만들었습니다.

```java
	if(SeatChoice_1.th1e_btn_selected[index - 1])
         {
            SeatChoice_1.th1e_btn_selected[index - 1] = false;
            btn.setBackground(new Color(0x404040));
            SeatChoice_1.selected_cnt--;
            SeatChoice_1.ticket_price -= SeatChoice_1.th1e_btn_price[index - 1];
            SeatChoice_1.price_label.setText("일반: " + (PeopleCheck.adult_cnt + PeopleCheck.child_cnt + PeopleCheck.old_cnt) + "              " + "장애인: " + PeopleCheck.disable_cnt + "              " + "가격: " + SeatChoice_1.ticket_price);

         }
         else
         {
            if(SeatChoice_1.peoples > SeatChoice_1.selected_cnt)
            {
               SeatChoice_1.th1e_btn_selected[index - 1] = true;
               btn.setBackground(new Color(0xFF3333));
               SeatChoice_1.selected_cnt++;
               SeatChoice_1.ticket_price += SeatChoice_1.th1e_btn_price[index - 1];
               SeatChoice_1.price_label.setText("일반: " + (PeopleCheck.adult_cnt + PeopleCheck.child_cnt + PeopleCheck.old_cnt) + "              " + "장애인: " + PeopleCheck.disable_cnt + "              " + "가격: " + SeatChoice_1.ticket_price);
            }
	
```

</details> 

<details>
	<summary>Duplicate selection error</summary>
	
> Problem
> > 인원수를 고르는 과정에서 인원수를 클릭한 뒤 마음이 바뀌어 다른 영화를 선택했을 때 인원수를 고르는 프레임에 기존에 클릭돼있던 버튼이 그대로 클릭되어있는 문제를 겪었었습니다
> > > Solution 
> > > > 매번 인원수를 고르는 프레임이 떴을때 마다 버튼들을 초기화해준다면 해결이 될 것이라고 생각했습니다<br>인원수를 고르다가 또는 좌석을 고르다가 다른 영화를 보고 싶어진 경우 이전으로 돌아가도 항상 0명에 버튼이 체크돼있도록 만들었습니다

```java
for(int i = 1; i < btns1.size(); i++) {
				adult_btn.get(i).setBackground(new Color(0x404040));
				child_btn.get(i).setBackground(new Color(0x404040));
				disable_btn.get(i).setBackground(new Color(0x404040));
				old_btn.get(i).setBackground(new Color(0x404040));
			}
			adult_cnt = 0;
			child_cnt = 0;
			disable_cnt = 0;
			old_cnt = 0;
			pre_adult_btn_num = 0;
			now_adult_btn_num = 0;
			pre_child_btn_num = 0;
			now_child_btn_num = 0;
			pre_disable_btn_num = 0;
			now_disable_btn_num = 0;
			pre_old_btn_num = 0;
			now_old_btn_num = 0;

		adult_btn.get(0).setBackground(new Color(0xCC0066));
		child_btn.get(0).setBackground(new Color(0xCC0066));
		disable_btn.get(0).setBackground(new Color(0xCC0066));
		old_btn.get(0).setBackground(new Color(0xCC0066));
	
```

</details><details>
	<summary>Cancel Seats & Rollback Button</summary>

```java

	
```

</details><details>
	<summary>Cancel Seats & Rollback Button</summary>

```java

	
```

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
 
*** 

## 📌 _Video Solution_
- Java Swing 동영상 출력

  - javaFx 외부라이브러리를 통한 동영상 출력
  
  ![오류](https://user-images.githubusercontent.com/84116965/129397173-add4f35f-7aec-4145-b7d3-75567cd09e58.png)
 
  - java 11.0.1버전은 해당 외부라이브러리와 연동문제가 생김 -> GIF파일로 대체하여 재생	
	
*** 

## 📸 _Demonstration Video_   
<details>
<summary>GUI 화면 영상</summary>
<div markdown="1">

영상삽입  


</div>
</details>   





