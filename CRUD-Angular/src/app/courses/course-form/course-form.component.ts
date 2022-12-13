import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../models/course';
import { CoursesService } from '../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  public form: FormGroup;

  constructor(
    private formBiulder: FormBuilder,
    private service: CoursesService,
    private dialog: MatDialog
  ) {
    this.form = this.formBiulder.group({
      name: [null],
      category: [null],
      duration: [null]
    })
  }

  onSubmit() {
    this.service.save(this.form.value).subscribe(
      {
      next(result):Course {
        console.log(result);
        return result
        this.complete
      },
      error(msg) {
        console.log('Error Getting Course: ', msg);
        this.error;
      },
      complete() {
        this.dialog.open(ErrorDialogComponent, {
          data: "Erro ao salvar Curso! Contate o Support."
        })
      },
    }
      )
  }


  onError(MsgError: String) {
    this.dialog.open(ErrorDialogComponent, {
      data: "Erro ao salvar Curso! Contate o Support."
    })
    // console.log(MsgError)
  }

  onCancel() { };

  ngOnInit(): void { };

}
