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
> > 인원수를 고르는 과정에서 인원수를 클릭한 뒤 마음이 바뀌어 다른 영화를 선택했을 때 <br>인원수를 고르는 프레임에 기존에 클릭돼있던 버튼이 그대로 클릭되어있는 문제를 겪었었습니다
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

</details>
	
<details>
	<summary>Check Type Verification</summary>   
	
> Problem
> > 좌석 선택중 장애인석의 숫자는 한정적인데 장애인이 아닌 사람이 장애인석을 예약하는 경우 오류 메시지를 띄워야 된다고 생각했으나<br> 사람 인원 중에서 장애인의 숫자를 알 수가 없어서 문제였습니다
> > > Solution 
> > > > 인원수를 전체인원이 아닌 장애인 인원을 변수에 따로 저장해두어 인원 수를 확인하면 될 것이라고 생각했습니다<br>장애인 인원수보다 많은 수를 예약하려고 하면 에러 메시지를 나오게 설정해두어서 장애인석은 장애인만 예약할 수 있게 했습니다

```java
if(PeopleCheck.disable_cnt == 0)
                  {
                     ErrorFrame frame = new ErrorFrame();
                     frame.getContentPane().setBackground(new Color(0x404040));
                     frame.setDefaultOptions();
                     JLabel label = new JLabel();
                     label.setText("장애인만 예약 가능합니다.");
                     label.setFont(new Font("돋움", Font.PLAIN|Font.BOLD, 30));
                     label.setForeground(Color.white);
                     label.setHorizontalAlignment(JLabel.CENTER);
                     frame.add(label);
                  }
                  else
                  {
                     if(PeopleCheck.disable_cnt > SeatChoice_1.disable_btn_cnt)
                     {
                        SeatChoice_1.th1a_btn_selected[index - 1] = true;
                        btn.setBackground(new Color(0xFF3333));
                        SeatChoice_1.disable_btn_cnt++;
                        SeatChoice_1.selected_cnt++;
                        SeatChoice_1.ticket_price += SeatChoice_1.th1a_btn_price[index - 1];
                        SeatChoice_1.price_label.setText("일반: " + (PeopleCheck.adult_cnt + PeopleCheck.child_cnt + PeopleCheck.old_cnt) + "              " + "장애인: " + PeopleCheck.disable_cnt + "              " + "가격: " + SeatChoice_1.ticket_price);
                     }
                     else
                     {
                        ErrorFrame frame = new ErrorFrame();
                        frame.getContentPane().setBackground(new Color(0x404040));
                        frame.setDefaultOptions();
                        JLabel label = new JLabel();
                        label.setText("장애인만 예약 가능합니다.");
                        label.setFont(new Font("돋움", Font.PLAIN|Font.BOLD, 30));
                        label.setForeground(Color.white);
                        label.setHorizontalAlignment(JLabel.CENTER);
                        frame.add(label);
                     }
	
```

</details>

<details>
	<summary>Exception in thread "AWT-EventQueue-0" java.lang.NumberFormatException: null</summary>    
	
> Problem
> > 생성자에서 date(일별 날짜) 값을 받아온 후 달력에서 날짜의 숫자가 한 자리일 때 앞에 "0"이 붙여질 수 있도록 생성해놓은
 getSales() 함수에서 date값을 사용해야 하는데, 생성자에 선언한 date 이전에 getSales() 함수를 불러왔기 때문에 null값이 나온다.
> > > Solution 
> > > > this.date = date; 밑에 getSales();를 입력해주어야 오류가 해결이 된다.

```java
public S2Panel3(String date) {
		this.date = date;
		getSales();
		setBackground(Color.CYAN);
		setBounds(12, 229, 362, 134);
		setLayout(null);
		l1 = new JLabel("상 품");
		l2 = new JLabel("수량 : " + count);
		l3 = new JLabel("가격 : " + sales);
		
		l1.setFont(new Font("굴림", Font.PLAIN, 50));
		l1.setHorizontalAlignment(SwingConstants.CENTER);
		l1.setBounds(12, 10, 140, 114);
		
		l2.setFont(new Font("굴림", Font.PLAIN, 20));
		l2.setBounds(164, 10, 200, 50);
		
		l3.setFont(new Font("굴림", Font.PLAIN, 20));
		l3.setBounds(164, 70, 200, 50);
		
		add(l1);
		add(l2);
		add(l3);
	}
	
```

</details>
	
<details>
	<summary>Design Size Error</summary>

- 상품들을 타입별로 나눠서 버튼으로 만들어주는 메소드들이다.
- 처음에는 버튼에 이미지와 글(가격, 이름)로 두개로만 메소드를 나눠서 했었다.
- 두개로만 했을때는 이미지의 사이즈를 줄이는데 제각각으로 바껴서 디자인에 오류가 생겼다.
- 또한 버튼에 글 작성하는 방법이 JLabel이 있었는데 JLabel로 여러개 나눠서 하는것보다 <br>html로 하는 방법이 효율적이라 생각해서 html로 만들어주는 메소드를 만들었다.
   
```java
/**
	products들의 이름과 가격를 gui에 보여주기위해 html를 활용해 text를 만들었다.
	@param name : 제품들 이름
	@param price : 제품들 가격
	@return : ArrayList<String>
 */
public ArrayList<String> p_text(ArrayList<String> name, ArrayList<Integer> price) {
	ArrayList<String> result = new ArrayList<>();
	
    for (int i = 0; i < name.size(); ++i) {
		DecimalFormat formatter = new DecimalFormat("###,###");	
		result.add("<HTML>" + name.get(i) + "<br>" + formatter.format(price.get(i)) + "원</HTML>");
	}
	return result;
}
	
/**
	ImageIcon ArrayList에 img_path의 사진을 넣어준다.
	img사이즈도 줄어줌
	@param image_paths : 여러 이미지 path들이 들어가 있음
	@return ArrayList<ImageIcon>
*/
public ArrayList<ImageIcon> makeImageIconArray(ArrayList<String> image_paths) {
	ArrayList<ImageIcon> icons = new ArrayList<>();
    
	for (String path : image_paths) {
		ImageIcon originIcon = new ImageIcon(path);
		Image resizeIcon = originIcon.getImage().getScaledInstance(150, 150, Image.SCALE_SMOOTH);
		
		icons.add(new ImageIcon(resizeIcon));
	}
	return icons;
}

/**
	img와 위에서 만든 name, price있는 text를 가지고 여러개의 버튼 만들기
	@param icons : 각각의 제품 img들이 들어있다.
	@param texts : 각각의 제품 name, price들이 들어있다.
	@return ArrayList<JButton>
*/
public ArrayList<JButton> btn_list(ArrayList<ImageIcon> icons, ArrayList<String> texts){
	ArrayList<JButton> btns = new ArrayList<>();
	
	for (int i = 0; i < icons.size(); ++i) {
		btns.add(new JButton(texts.get(i),icons.get(i)));
		btns.get(i).setBackground(Color.white);
	}
	return btns;
}

/**
 	타입에 맞는 products들의 정보 가져와서 ArrayList에 담아주기
 	@param products ArrayList에 제품 정보 담기
	@param typeName 선택된 상품 type
	@return ArrayList<Products>
*/
public ArrayList<Products> typeOfproduct(ArrayList<Products> products, String typeName){
	ArrayList<Products> array = new ArrayList<>();

	for (int i = 0; i < products.size(); ++i) {
		if (products.get(i).getType().equals(typeName)) {
			array.add(products.get(i));
		}
	}
	return array;
}
```

</details>
	
<details>
	<summary>Get movie information</summary>

> Problem
> > 영화 시간을 선택하면 그에 따른 영화 정보와 다른 정보들이 같이 와야 하는 상황이 있었는데<br>
버튼에서 가져올 수 있는것은 영화가 시작하는 시간 하나라서 이것으로 다른 정보들을 연결해서 찾기가 어려웠다<br> 
만약 같은 시간대에 상영하는 다른 영화들이 존재하면 어떤 영화의 시간인지 알 수 없기에 원하는 정보를 얻을 수 없었다<br>
> > > Solution 
> > > > 버튼을 만들 때 영화마다 영화 정보가 담겨있는 클래스를 따로 만들어서 <br>
버튼의 리스너 기능을 추가할 때 그에 맞는 영화 클래스 정보를 담아 놓는 방법을 선택했다<br>
1번 영화를 선택하면 버튼이 구현되어 있는 클래스 자체에 1번 영화의 정보를 담아 놓고
시간 정보는 버튼의 이름에 설정해놓은 다음<br>
버튼을 클릭하면 1번 영화가 담겨져 있는 클래스로 넘어가고<br>
클래스에는 이미 데이터베이스에서 가져온 시간 정보와 영화 정보들이 담겨 있기에<br>
시간대를 비교해서 해당 영화가 가지고 있는 다른 정보들을 가져오는 방식을 사용했다<br>
   
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





