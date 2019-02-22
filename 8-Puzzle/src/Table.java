//Brian Fox and Greg Walsh
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
	
	/**
	 * set value for the first row of table 
	 */
	public void setHeadings(String[] headings) {
		if(headings.length == width) {
			this.headings = headings;
		}else {
			throw new IllegalArgumentException("Must have exactly one heading for each collumn");
		}
	}
	
	/**
	 * fill next cell in table in the order left --> right,top --> bottom
	 */
	public void fill(String val) {
		values[filled/width][filled%width] = val;
		filled ++;
	}
	
	/**
	 * align elements to collumn and return table as single string
	 * @return string representation of rows seperated by newlines
	 */
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append(title);
		sb.append('\n');
		sb.append(String.format("%2s", headings[0]));
		for(int i =1;i<width;i++) {
			sb.append(String.format("%15s", headings[i]));
		}
		sb.append('\n');
		for(String[] rows : values) {
			sb.append(String.format("%2s", rows[0]));
			for(int i =1;i<width;i++) {
				sb.append(String.format("%15s", rows[i]));
			}
			sb.append('\n');
		}
		
		return (sb.toString());
	}
	
}
