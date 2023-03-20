def smoking_status_by_stroke(data, stroke):
  list_by_stroke = list(filter(lambda item: item['stroke'] == stroke, data))
  smoking_count = {"formerly smoked": 0, "never smoked": 0, "smokes": 0, "Unknown": 0}
  print(list_by_stroke[0])

  for person in list_by_stroke:
    smoking_status = person['smoking_status']
    smoking_count[smoking_status] += 1

  print(smoking_count)
  labels = smoking_count.keys()
  values = smoking_count.values()
  
  return labels, values