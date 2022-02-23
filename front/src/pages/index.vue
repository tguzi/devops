<template>
  <el-container class="layout-container">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-scrollbar>
        <el-menu :default-openeds="['1', '3']">
          <el-sub-menu index="1">
            <template #title>
              <el-icon><IconMenu /></el-icon>导航
            </template>
            <el-menu-item-group>
              <el-menu-item>分支流水</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <div class="toolbar">
          <el-dropdown>
            <el-icon style="margin-right: 8px; margin-top: 1px"><setting /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>查看</el-dropdown-item>
                <el-dropdown-item>退出</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <span>用户名</span>
        </div>
      </el-header>
      <el-main>
        <el-scrollbar>
          <el-row :gutter="12">
            <el-col :span="8">
              <el-card shadow="always">测试环境</el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">预发环境</el-card>
            </el-col>
            <el-col :span="8">
              <el-card shadow="always">线上环境</el-card>
            </el-col>
          </el-row>
          <br />
          <el-card>
            <el-row :gutter="2">
              <el-col :span="6">
                <el-progress type="dashboard" :percentage="80">
                  <template #default="{ percentage }">
                    <span class="percentage-value">{{ percentage }}%</span>
                    <br />
                    <span class="percentage-label">分支管理</span>
                  </template>
                </el-progress>
              </el-col>
              <el-col :span="6">
                <el-progress type="dashboard" :percentage="80">
                  <template #default="{ percentage }">
                    <span class="percentage-value">{{ percentage }}%</span>
                    <br />
                    <span class="percentage-label">构建</span>
                  </template>
                </el-progress>
              </el-col>
              <el-col :span="6">
                <el-progress type="dashboard" :percentage="80">
                  <template #default="{ percentage }">
                    <span class="percentage-value">{{ percentage }}%</span>
                    <br />
                    <span class="percentage-label">发布</span>
                  </template>
                </el-progress>
              </el-col>
            </el-row>
          </el-card>
          <br />
          <el-card>
            <el-button type="primary" @click="dialogVisible = true">新建</el-button>
            <br />
            <br />
            <el-table :data="tableData" stripe border style="width: 100%">
              <el-table-column prop="demand" label="需求" />
              <el-table-column prop="developer" label="开发人员" />
              <el-table-column prop="branch" label="分支" />
              <el-table-column prop="commit" label="预览代码" />
              <el-table-column fixed="right" label="Operations" width="120">
                <template #default>
                  <el-button type="text" size="small" @click="addToFlow">加入集成</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
          <br />
          <el-card>
            <el-button type="primary" @click="publish">点击发布</el-button>
            &nbsp;&nbsp;
            <span>当前分支： featrue-128129-218919</span>
            <br />
            <br />
            <el-table :data="tableData" stripe border style="width: 100%">
              <el-table-column prop="demand" label="需求" />
              <el-table-column prop="developer" label="开发人员" />
              <el-table-column prop="branch" label="分支" />
              <el-table-column prop="commit" label="预览代码" />
              <el-table-column fixed="right" label="Operations" width="120">
                <template #default>
                  <el-button type="text" size="small" @click="exitFlow">退出集成</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </el-scrollbar>
      </el-main>
    </el-container>
  </el-container>
  <el-dialog v-model="dialogVisible" title="新建需求" destroy-on-close center>
    <el-form ref="formRef" :model="form" label-width="120px">
      <el-form-item label="开发人员">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="测试人员">
        <el-select v-model="form.region" placeholder="请选择测试">
          <el-option label="测试1" value="shanghai"></el-option>
          <el-option label="测试1" value="beijing"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="预计发布时间">
        <el-date-picker v-model="form.date1" type="date" placeholder="选择时间" />
      </el-form-item>
      <el-form-item label="分支名">
        <el-row>
          <el-col :span="5">featrure-</el-col>
          <el-col :span="6"><el-input v-model="form.name"></el-input></el-col>
          <el-col :span="10">-{{ currentTime }}</el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="需求描述">
        <el-input v-model="form.desc" type="textarea"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script lang="ts" setup>
  import { ref, reactive, onMounted } from 'vue'
  import request from '../request'
  const dialogVisible = ref(false)
  const currentTime = ref(Date.now())
  const form = reactive({
    name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: ''
  })
  onMounted(() => {
    // http://localhost:8000/api/workflow/init
    request.get('/api/workflow/init').then((res) => {
      console.log('1111', res)
    })
  })
  const tableData = [
    {
      developer: 'wqf',
      branch: 'feature-sxxx-12312',
      commit: 'asldka1238sks',
      demand: '需求'
    }
  ]
  const addToFlow = () => {
    console.log('加入集成')
  }
  const exitFlow = () => {
    console.log('退出集成')
  }
  const publish = () => {
    console.log('点击发布')
  }
</script>

<style lang="less" scope>
  .layout-container {
    width: 100vw;
    height: 100vh;
    box-sizing: border-box;
    overflow: hidden;
    .el-header {
      position: relative;
      background-color: #b3c0d1;
      color: var(--el-text-color-primary);
    }
    .el-aside {
      width: 240px;
      color: var(--el-text-color-primary);
      background: #fff !important;
      border-right: solid 1px #e6e6e6;
      box-sizing: border-box;
    }
    .el-menu {
      border-right: none;
    }
    .el-main {
      padding: 0;
    }
    .el-scrollbar {
      padding: 20px;
    }
    .toolbar {
      position: absolute;
      display: inline-flex;
      align-items: center;
      top: 50%;
      right: 20px;
      transform: translateY(-50%);
    }
  }
</style>
