var kanha = ee.Geometry.Rectangle([80.53, 22.05, 81.20, 22.45]);

var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(kanha)
  .filterDate('2023-01-01', '2023-12-31')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .median()
  .clip(kanha);

Export.image.toDrive({
  image: s2.select(['B4', 'B5']),
  description: 'Kanha_B4_B5',
  scale: 10,
  region: kanha,
  maxPixels: 1e13
});
