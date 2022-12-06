import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

import { CoursesService } from '../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  form: FormGroup

  constructor(
    private formBiulder: FormBuilder,
    private courseService: CoursesService,
    ) {
    this.form = formBiulder.group({
      name: [null],
      category: [null]
    })
  }

  onSubmit() { 
    this.courseService.save(this.form.value)
    // console.log(this.form.value)

  }

  onCancel() { }

  ngOnInit(): void {
  }

}
