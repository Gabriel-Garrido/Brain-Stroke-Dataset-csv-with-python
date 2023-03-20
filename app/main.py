import utils
import read_csv
import charts

def run():
  stroke = input('Show person with stroke(1), without stroke (0)')
  data = read_csv.read_csv('./app/data.csv')
  labels, values = utils.smoking_status_by_stroke(data, stroke)
  print(labels, values)
  charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()