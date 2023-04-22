import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'name'
})
export class NamePipe implements PipeTransform {

  transform(value: String): String {

    switch (value) {
      case 'Angular': return 'code';
      case 'Spring': return 'data_object';
      case 'Angular + Spring': return 'developer_mode';
      case 'Massoterapia': return 'volunteer_activism';

      default: { return '' };

    }
  }
}
