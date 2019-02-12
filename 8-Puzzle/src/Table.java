
public class Table {
	private int width;
	private int height;
	private String[][] values;
	private String[] headings;
	private String title;
	private int filled;
	
	public Table(int width, int height) {
		this.width = width;
		this.height = height;
		this.values = new String[height][width];
		this.title = "";
		this.headings = new String[width];
		this.filled=0;
	}
	
	public Table(int width,int height,String title) {
		this(width,height);
		this.title = title;
	}
	
	public void setHeadings(String[] headings) {
		if(headings.length == width) {
			this.headings = headings;
		}else {
			throw new IllegalArgumentException("Must have exactly one heading for each collumn");
		}
	}
	
	public void fill(String val) {
		values[filled/width][filled%width] = val;
		filled ++;
	}
	
	public void print() {
		StringBuilder sb = new StringBuilder();
		sb.append(title);
		sb.append('\n');
		sb.append(String.format("%2s", headings[0]));
		for(int i =1;i<width;i++) {
			sb.append(String.format("%15s", headings[i]));
			//sb.append("\t\t");
		}
		sb.append('\n');
		for(String[] rows : values) {
			sb.append(String.format("%2s", rows[0]));
			for(int i =1;i<width;i++) {
				sb.append(String.format("%15s", rows[i]));
				//sb.append("\t\t");
			}
			sb.append('\n');
		}
		
		System.out.print(sb.toString());
	}
	
}
